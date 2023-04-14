# Delete, destroy, delete_all, destroy_all
Imagine I have a model called `model` and it `has_many: child`. Explain what the following 4 lines of code do, in particular with regards to callbacks and the :dependent option:
```
  model.delete
  model.destroy
  model.childs.delete_all 
  model.childs.destroy_all
```
Here's a breakdown of what each line of code does, with regards to callbacks and the :dependent option:

model.delete:
 * This line of code deletes the model instance directly from the database.
 * It does not run any callbacks or validations defined in the model.
 * It also does not affect the associated child records, regardless of the :dependent option specified in the has_many relationship.

model.destroy:
 * This line of code destroys the model instance, running any before_destroy and after_destroy callbacks defined in the model.
 * It also respects the :dependent option specified in the has_many relationship. If the :dependent option is set to :destroy, it will destroy all associated child records, running their callbacks as well. If the :dependent option is set to :delete_all, it will delete all associated child records without running their callbacks. If the :dependent option is set to :nullify, it will set the foreign key in the associated child records to NULL.

model.childs.delete_all:
 * This line of code deletes all associated child records directly from the database.
 * It does not run any callbacks or validations defined in the child model.
 * It also does not affect the model instance, and it does not respect the :dependent option specified in the has_many relationship.

model.childs.destroy_all:
 * This line of code destroys all associated child records, running any before_destroy and after_destroy callbacks defined in the child model.
 * It does not affect the model instance, and it does not respect the :dependent option specified in the has_many relationship.
 * It differs from model.childs.delete_all in that it runs the callbacks on the associated child records before destroying them.
