# Model

## Constraints in abstract base classes

| You must always specify a unique name for the constraint. As such, you cannot normally specify a constraint on an abstract base class, since the Meta.constraints option is inherited by subclasses, with exactly the same values for the attributes (including name) each time. To work around name collisions, part of the name may contain '%(app_label)s' and '%(class)s', which are replaced, respectively, by the lowercased app label and class name of the concrete model. For example CheckConstraint(check=Q(age__gte=18), name='%(app_label)s_%(class)s_is_adult').

[reference - django docs](https://docs.djangoproject.com/en/4.0/ref/models/constraints/)