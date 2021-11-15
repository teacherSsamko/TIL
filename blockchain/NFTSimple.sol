// Klaytn IDE uses solidity 0.4.24, 0.5.6 versions.
pragma solidity >=0.4.24 <=0.5.6;

contract NFTSimple {
    string public name = "KlaySsamko";
    string public symbol = "KL";

    mapping(uint256 => address) public tokenOwner;
    mapping(uint256 => string) public tokenURIs;

    // tokenOwner list
    mapping(address => uint256[]) private _ownedTokens;
    // onKIP17Recieved bytes value
    bytes4 private constant _KIP17_RECEIVED = 0x6745782b;

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
        uint256 tokenId,
        bytes memory _data
    ) public {
        require(from == msg.sender, "from != msg.sender");
        require(from == tokenOwner[tokenId], "you are not owner of the token");

        _removeTokenFromList(from, tokenId);
        _ownedTokens[to].push(tokenId);

        tokenOwner[tokenId] = to;

        // If Receiver has some code to implements when recieved, execute codes
        require(
            _checkOnKIP17Received(from, to, tokenId, _data),
            "KIP17: transfer to non KIP17Receiver implementer"
        );
    }

    function _checkOnKIP17Received(
        address from,
        address to,
        uint256 tokenId,
        bytes memory _data
    ) internal returns (bool) {
        bool success;
        bytes memory returndata;

        if (!isContract(to)) {
            return true;
        }

        (success, returndata) = to.call(
            abi.encodeWithSelector(
                _KIP17_RECEIVED,
                msg.sender,
                from,
                tokenId,
                _data
            )
        );
        if (
            returndata.length != 0 &&
            abi.decode(returndata, (bytes4)) == _KIP17_RECEIVED
        ) {
            return true;
        }

        return false;
    }

    function isContract(address account) internal view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(account)
        }
        return size > 0;
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
    mapping(uint256 => address) public seller;

    function buyNFT(uint256 tokenId, address NFTAddress)
        public
        payable
        returns (bool)
    {
        // send 0.01 klay to buyer
        address payable receiver = address(uint160(seller[tokenId]));

        // send 0.01 klay to receiver
        // 10 ** 18 peb = 1 klay
        // 10 ** 16 peb = 0.01 klay
        receiver.transfer(10**16);

        NFTSimple(NFTAddress).safeTransferfrom(
            address(this),
            msg.sender,
            tokenId,
            "0x00"
        );

        return true;
    }

    // when Market is received token(NFT is on sale), store who want to sell it
    function onKIP17Received(
        address operator,
        address from,
        uint256 tokenId,
        bytes memory data
    ) public returns (bytes4) {
        seller[tokenId] = from;
        return
            bytes4(keccak256("onKIP17Received(address,address,uint256,bytes)"));
    }
}
