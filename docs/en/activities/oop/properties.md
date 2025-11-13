# Properties

In the `pylib.pyflix.mediatheque` module, you will find a `TvShow` class. This class represents 
a television show or in our case a television series. For now, the attributes are public.

First, check the compliance to the specifications:

 * The title is an attribute named `name` in lower case, the first letter of each word must be 
   uppercase.
 * You can get the list of all episodes with an attribute.
 * An episode is added with the `add_episode()` method.
 * Duplication of episodes is prevented by raising an exception.

Then, make sure that:

* The content of the episodes list must not be altered by its attribute. Only by calling the method.
* If the title is modified (with `myshow.name = 'New title'`), the letter case rule must be applied.
* We should get the series duration with an attribute.

Update the other classes if needed.