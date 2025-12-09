# Properties

The module `pylib.pyflix.mediatheque` contains a class `TvShow` which represents a television 
series. For now, all the attributes are public.

First, check the specifications:

 * The title is an attribute `name` with all words first letter in uppercase and the rest in lowercase.
 * The list of the episodes is returned with an attribute
 * An episode is added with the method `add_episode()`
 * Added an existing episode must raise an exception.

Then, you must make sure that:

 * The list of the episodes must not be altered by its attribute, only through the method.
 * If the title is set trough its attribute, the type case must follow the specifications.
 * We must get the series duration using an attribute

Update if needed the other classes from the module.