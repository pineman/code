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

model.childs.delete_all: -- É UMA ASSOCIATION
 * This line of code deletes all associated child records directly from the database.
 * It does not run any callbacks or validations defined in the child model.
 * It also does not affect the model instance, and it does not respect the :dependent option specified in the has_many relationship.

model.childs.destroy_all: -- É UMA ASSOCIATION
 * This line of code destroys all associated child records, running any before_destroy and after_destroy callbacks defined in the child model.
 * It does not affect the model instance, and it does not respect the :dependent option specified in the has_many relationship.
 * It differs from model.childs.delete_all in that it runs the callbacks on the associated child records before destroying them.
------------------------------------------------------------
ActiveRecord::Persistence:
 * delete - Deletes the record in the database and freezes this instance to reflect that no changes should be made (since they can't be persisted). Returns the frozen instance. To enforce the object's before_destroy and after_destroy callbacks or any :dependent association options, use destroy.
 * destroy - Deletes the record in the database and freezes this instance to reflect that no changes should be made (since they can't be persisted). There's a series of callbacks associated with destroy. If the before_destroy callback throws :abort the action is cancelled and destroy returns false.

ActiveRecord::Associations::CollectionProxy
 * delete - Deletes the records supplied from the collection according to the strategy specified by the :dependent option. If no :dependent option is given, then it will follow the default strategy. Returns an array with the deleted records.
 * destroy - Destroys the records supplied and removes them from the collection. This method will always remove record from the database ignoring the :dependent option. Returns an array with the removed records.
 * delete_all - Deletes all the records from the collection according to the strategy specified by the :dependent option. If no :dependent option is given, then it will follow the default strategy.
 * destroy_all - Deletes the records of the collection directly from the database ignoring the :dependent option. Records are instantiated and it invokes before_remove, after_remove, before_destroy, and after_destroy callbacks.

ActiveRecord::Relation:
 * delete_all - Deletes the records without instantiating the records first, and hence not calling the #destroy method nor invoking callbacks. This is a single SQL DELETE statement that goes straight to the database, much more efficient than destroy_all. Be careful with relations though, in particular :dependent rules defined on associations are not honored. Returns the number of rows affected.
 * destroy_all - Destroys the records by instantiating each record and calling its #destroy method. Each object's callbacks are executed (including :dependent association options). Returns the collection of objects that were destroyed; each will be frozen, to reflect that no changes should be made (since they can't be persisted). Note: Instantiation, callback execution, and deletion of each record can be time consuming when you're removing many records at once. It generates at least one SQL DELETE query per record (or possibly more, to enforce your callbacks). If you want to delete many rows quickly, without concern for their associations or callbacks, use delete_all instead.
--------------------------------------------------------
When you define a has_many association with the :dependent option in a Rails model, you can choose between :destroy and :delete_all as the strategy for handling associated records when the parent record is deleted. Here's an explanation of how each strategy works and how they affect the model's children's :dependent options:

has_many :model, dependent: :destroy

With this option, when the parent record is destroyed, Rails will instantiate each associated record, run their before_destroy and after_destroy callbacks, and then destroy the record. If any of the associated records has its own associations with :dependent options, those options will also be respected and executed accordingly.

In this case, if an associated record has its own child records with :dependent options, the destruction process will cascade down the chain, ensuring that all :dependent options are respected.

has_many :model, dependent: :delete_all

With this option, when the parent record is destroyed, Rails will directly delete all the associated records from the database without instantiating the objects or running any callbacks. As a result, the :dependent options of the associated records' children will NOT be respected.

In this case, if an associated record has its own child records with :dependent options, those options will be ignored, and the records will be left orphaned in the database. This can lead to data inconsistency and orphaned records.

In summary, has_many :model, dependent: :destroy will respect the :dependent options of the associated records' children, running callbacks and cascading the destruction process down the chain. On the other hand, has_many :model, dependent: :delete_all will not respect the :dependent options of the associated records' children, directly deleting the records from the database without running callbacks. This can result in orphaned records and data inconsistency.
