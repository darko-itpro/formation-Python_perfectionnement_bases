potter_movies = [["The Philosopher's Stone", 152, True],
                 ["The Chamber of Secrets", 161, True],
                 ["The Prisoner of Azkaban", 142, False],
                 ["the Goblet of Fire", 157, True],
                 ["the Order of the Phoenix", 138, False],
                 ["the Half-Blood Prince", 153, True],
                 ["the Deathly Hallows – Part 1", 126, False],
                 ("the Deathly Hallows – Part 2", 130, False)]

movies_titles = [title for title, *_ in potter_movies]
print(movies_titles)

titles_to_view = [title for title, _, viewed in potter_movies if not viewed]
print(titles_to_view)

duration = sum([duration for _, duration, _ in potter_movies])

print("Durée : {:02}h{:02}".format(*divmod(sum([duration for _, duration, _ in potter_movies]), 60)))