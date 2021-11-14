// Klaytn IDE uses solidity 0.4.24, 0.5.6 versions.
pragma solidity >=0.4.24 <=0.5.6;

contract NFTSimple {
    string public name = "KlaySsamko";
    string public symbol = "KL";

    mapping(uint256 => address) public tokenOwner;
    mapping(uint256 => string) public tokenURIs;

    // tokenOwner list
    mapping(address => uint256[]) private _ownedTokens;

    // mint(tokenId, uri, owner)
    // transferfrom(from, to, tokenId)

    function mintWithTokenURI(
        address to,
        uint256 tokenId,
        string memory tokenURI
    ) public returns (bool) {
        // mint a token with tokenId to 'to'
        tokenOwner[tokenId] = to;
        tokenURIs[tokenId] = tokenURI;

        // add token to the list
        _ownedTokens[to].push(tokenId);

        return true;
    }

    function safeTransferfrom(
        address from,
        address to,
        uint256 tokenId
    ) public {
        require(from == msg.sender, "from != msg.sender");
        require(from == tokenOwner[tokenId], "you are not owner of the token");

        _removeTokenFromList(from, tokenId);
        _ownedTokens[to].push(tokenId);

        tokenOwner[tokenId] = to;
    }

    function _removeTokenFromList(address from, uint256 tokenId) private {
        // [10, 15, 19, 20] -> want to remove 19
        // [10, 15, 20, 19] -> slice
        // [10, 15, 20]
        uint256 lastIdx = _ownedTokens[from].length - 1;
        for (uint256 i = 0; i < _ownedTokens[from].length; i++) {
            if (tokenId == _ownedTokens[from][i]) {
                _ownedTokens[from][i] = _ownedTokens[from][lastIdx];
                _ownedTokens[from][lastIdx] = tokenId;
                break;
            }
        }
        _ownedTokens[from].length--;
    }

    function ownedTokens(address owner) public view returns (uint256[] memory) {
        return _ownedTokens[owner];
    }

    function setTokenUri(uint256 id, string memory uri) public {
        tokenURIs[id] = uri;
    }
}

contract NFTMarket {
    function buyNFT(
        uint256 tokenId,
        address NFTAddress,
        address to
    ) public returns (bool) {
        NFTSimple(NFTAddress).safeTransferfrom(address(this), to, tokenId);

        return true;
    }
}
