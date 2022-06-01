class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps


recipe1 = Recipe('\033[1m' + 'Mac and Cheese' + '\033[0m',
                 '\nINGREDIENTS'
                 '\n2 tsp salt '
                 '\n1 lb [455 g] elbow macaroni'
                 '\n2 cups [480 ml] whole milk'
                 '\n1 cup [240 ml] heavy cream'
                 '\n1 stick unsalted butter'
                 '\n1/4 cup [35 g] all-purpose flour'
                 '\n4 cups HAND SHREDDED shredded sharp Cheddar cheese'
                 '\n2 cups HAND SHREDDED Jarlsberg cheese'
                 '\n2/3 cup [80 g] sour cream'
                 '\n1 tsp cracked black pepper'
                 '\n2 tsp dry mustard'
                 '\n1/2 tsp ground nutmeg'
                 '\n2 tsp Worcestershire sauce'
                 '\n1-2 tsp cayenne pepper'
                 '\n1 cup Panko breadcrumbs',
                 '\n'
                 '\nSTEPS'
                 '\n1. Preheat the oven to 400°F [200°C], with a rack in the middle position'
                 '\n2. Shred all the cheese'
                 '\n3. Bring a large pot of heavily salted water to a boil. Add the macaroni and cook until al dente, about 1 minute less than the package instructions. Drain and set aside. '
                 '\n4. In a large skillet over medium heat, melt 4tbsp butter. Sprinkle in the flour and whisk constantly for 2 to 3 minutes. Gradually whisk in the milk and cream. Cook for 2 minutes, whisking frequently, or until thickened and smooth. (Adjust the heat to keep the milk from boiling). '
                 '\n5. Gradually add half of the shredded cheese, whisking until fully incorporated and smooth. Add the sour cream and whisk until smooth. Add the pepper, dry mustard, cayenne, and Worcestershire sauce. Season with salt.'
                 '\n6. Mix 4tbsp butter and 1 cup breadcrumbs'
                 '\n7. Add the cooked macaroni to the cheese sauce and stir until combined. Spoon half of the mixture into the prepared baking dish. Top evenly with the remaining cheese. Then add the rest of the mac. Top with breadcrumbs and sprinkle cayenne on top. Bake for 25 to 30 minutes.'
                 '\n8. Let rest for 10 minutes before consuming')

print(recipe1.name, recipe1.ingredients, recipe1.steps)