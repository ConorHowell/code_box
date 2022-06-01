import random
import requests


# https://discord.com/api/v9/channels/979618941162881026/messages


class Recipe:
    instances = []

    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        __class__.instances.append(self)


mac = Recipe('Mac and Cheese',
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
             '\n3. Bring a large pot of heavily salted water to a boil. Add the macaroni and cook until al dente, about 1 minute less than the package instructions. '
             '\n   Drain and set aside. '
             '\n4. In a large skillet over medium heat, melt 4tbsp butter. '
             '\n   Sprinkle in the flour and whisk constantly for 2 to 3 minutes. Gradually whisk in the milk and cream. '
             '\n   Cook for 2 minutes, whisking frequently, or until thickened and smooth. (Adjust the heat to keep the milk from boiling). '
             '\n5. Gradually add half of the shredded cheese, whisking until fully incorporated and smooth. '
             '\n   Add the sour cream and whisk until smooth. '
             '\n   Add the pepper, dry mustard, cayenne, and Worcestershire sauce. Season with salt.'
             '\n6. Mix 4tbsp butter and 1 cup melted breadcrumbs'
             '\n7. Add the cooked macaroni to the cheese sauce and stir until combined. '
             '\n   Spoon half of the mixture into the prepared baking dish. Top evenly with the remaining cheese. '
             '\n   Then add the rest of the mac. Top with breadcrumbs and sprinkle cayenne on top. Bake for 25 to 30 minutes.'
             '\n8. Let rest for 10 minutes before consuming')

chili = Recipe('Chili',
               '\nINGREDIENTS'
               '\n2 pounds ground beef'
               '\n2 cloves garlic, chopped'
               '\nOne 8-ounce can tomato sauce'
               '\n2 tablespoons chili powder'
               '\n1 teaspoon ground cumin'
               '\n1 teaspoon ground oregano'
               '\n1 teaspoon salt'
               '\n1/4 teaspoon cayenne pepper'
               '\n1/4 cup masa harina'
               '\nOne 15-ounce can kidney beans, drained and rinsed'
               '\nOne 15-ounce can pinto beans, drained and rinsed'
               '\nShredded Cheddar, for serving'
               '\nChopped onions, for serving'
               '\nTortilla chips, for serving'
               '\nLime wedges, for serving',
               '\n'
               '\nSTEPS'
               '\n1. Place the ground beef in a large pot and throw in the garlic. Cook over medium heat until browned. '
               '\n   Drain off the excess fat, and then pour in the tomato sauce, chili powder, cumin, oregano, salt and cayenne. '
               '\n   Stir together well, cover, and then reduce the heat to low. Simmer for 1 hour, stirring occasionally. '
               '\n   If the mixture becomes overly dry, add 1/2 cup water at a time as needed. '
               '\n2. After an hour, place the masa harina in a small bowl. '
               '\n   Add 1/2 cup water and stir together with a fork. '
               '\n   Dump the masa mixture into the chili. Stir together well, and then taste and adjust the seasonings. '
               '\n   Add more masa paste and/or water to get the chili to your preferred consistency, or to add more corn flavor. '
               '\n   Add the beans and simmer for 10 minutes. Serve with shredded Cheddar, chopped onions, tortilla chips and lime wedges.')

marsala = Recipe('Chicken Marsala',
                 '\nINGREDIENTS'
                 '\n1 1/2 pounds boneless, skinless chicken breast halves, cut into roughly 1 x 2-inch, 3/8-inch-thick strips'
                 '\n1/4 cup all-purpose flour'
                 '\nKosher salt and freshly ground black pepper'
                 '\n4 tablespoons extra-virgin olive oil'
                 '\n2 cups tightly packed baby spinach leaves'
                 '\n3 cups sliced mushrooms'
                 '\n1 large red bell pepper, seeded and julienned'
                 '\n1/4 cup minced shallot'
                 '\n1 tablespoon tomato paste'
                 '\n2 garlic cloves, minced'
                 '\n1 teaspoon thyme leaves'
                 '\n1 cup sweet Marsala wine'
                 '\n1 cup chicken stock(low-sodium)'
                 '\n2 tablespoons cold unsalted butter, cut into cubes'
                 '\n3 tablespoons chopped flat-leaf parsley'
                 '\n1 pound of pasta',
                 '\n'
                 '\nSTEPS'
                 '\n1. Using the flat side of a meat mallet, lightly pound the chicken pieces'
                 '\n2. In a large dish, combine the flour, 1 teaspoon salt, and 1/2 teaspoon black pepper.'
                 '\n   Lightly dredge the chicken pieces in the flour and set aside'
                 '\n3. In a large nonstick saute pan over medium-high heat, heat 1 tablespoon of the olive oil.'
                 '\n   Saute the spinach until wilted, 1 to 2 minutes'
                 '\n   Season with salt and black pepper and set aside.'
                 '\n   Add 2 tablespoons of the olive oil to the pan and, working in batches, brown the chicken pieces all over, 3 to 6 minutes.'
                 '\n   Remove the chicken from the pan and set aside.'
                 '\n4. Add the remaining 1 tablespoon olive oil to the pan, then add the mushrooms, bell pepper, shallot, and salt to taste.'
                 '\n   Saute until the mushrooms are lightly browned, 6 to 8 minutes.'
                 '\n   Stir in the tomato paste, garlic, and thyme and cook for 1 minute, until fragrant. '
                 '\n   Deglaze by adding the Marsala and scraping up the browned bits from the bottom of the pan'
                 '\n5. Return the chicken to the pan, then add the chicken stock.'
                 '\n   Bring to a boil and simmer until reduced by half, 6 to 8 minutes.'
                 '\n   Season with salt and pepper and return the cooked spinach to the pan.'
                 '\n   Stir in the butter cubes a few at a time until melted.'
                 '\n   Stir in the parsley'
                 '\n6. Meanwhile, to cook the pasta, in a large stockpot over medium-high heat, bring 1 gallon of water to a boil.'
                 '\n   Add 1 tablespoon salt, then add the pasta.'
                 '\n   Cook according to the package directions (timing will vary depending on the pasta chosen) until al dente then drain.'
                 '\n7. Toss the pasta with the chicken and sauce then consume')

schnitzel = Recipe('Panko Chicken Schnitzel',
                   '\nINGREDIENTS'
                   '\n1/2 cup all-purpose flour'
                   '\n3 eggs, beaten'
                   '\n2 cups panko'
                   '\n4 skinless, boneless chicken breast halves (about 6 ounces each), butterflied and pounded 1/4-inch-thick'
                   '\nKosher salt and freshly ground pepper'
                   '\n1/2 cup canola oil'
                   '\n6 tablespoons butter'
                   '\n2 teaspoons capers'
                   '\n2 tablespoons fresh lemon juice'
                   '\n1 tablespoon chopped parsley',
                   '\n'
                   '\nSTEPS'
                   '\n1. Set the flour, eggs and panko in three separate shallow bowls. '
                   '\n   Season the chicken cutlets with salt and pepper.'
                   '\n   Dredge the chicken in the flour, shaking off any excess, then dip in the eggs and coat thoroughly with the panko, pressing lightly to adhere.'
                   '\n2. In each of 2 large skillets, heat 1/4 cup of canola oil. '
                   '\n   Add the chicken and cook over moderately high heat, turning once, until golden and crispy, about 3 minutes per side. '
                   '\n   Transfer the chicken to a paper towel-lined baking sheet and sprinkle with salt, then transfer to plate.'
                   '\n3. Meanwhile, in a small saucepan, melt the butter and cook over moderately high heat until browned and nutty, about 4 minutes. '
                   '\n   Stir in the capers, lemon juice and parsley; spoon over the chicken and serve.')

lasagna = Recipe('Lasagna',
                 '\nINGREDIENTS'
                 '\nSalt'
                 '\n1 pound lasagna sheets'
                 '\n8 ounces sliced pepperoni (about 2 cups)'
                 '\n4 cups Tomato Sauce, recipe follows'
                 '\n1 pound ricotta'
                 '\n1 pound shredded mozzarella'
                 '\n2 pounds bulk Italian sausage, cooked'
                 '\n3/4 cup grated Parmesan'
                 '\nSAUCE'
                 '\n3 tablespoons extra-virgin olive oil'
                 '\n1 yellow onion, diced'
                 '\n5 medium cloves garlic, minced'
                 '\nTwo 28-ounce cans crushed tomatoes'
                 '\n2 tablespoons thinly sliced fresh basil'
                 '\n1 tablespoon minced fresh oregano'
                 '\nSalt and freshly ground black pepper',
                 '\n'
                 '\nSTEPS'
                 '\n1. In a medium saucepan, heat the olive oil. '
                 '\n   Add the onions and cook over medium to low heat until transparent, about 20 minutes. '
                 '\n   Add the garlic and cook until almost brown, about 10 minutes. '
                 '\n   Then, add the tomatoes and cook for 30 minutes over low to medium heat. '
                 '\n   Add the basil and oregano and continue to cook for another 30 minutes. '
                 '\n   Season with salt and pepper, cool and store in the refrigerator until ready to use.'
                 '\n2. Preheat the oven to 375 degrees F.'
                 '\n3. Boil 6 quarts of water, add a pinch of salt and cook the pasta to almost done, about 7 minutes. '
                 '\n   Remove from the water and shock in an ice bath. '
                 '\n4. In a medium saucepan, add the pepperoni and saute over medium heat until crispy, about 10 minutes. '
                 '\n   Remove from the heat and drain on a paper towel. '
                 '\n5. In a 10- by 14- by 3-inch baking pan or dish, pour 1 cup of the Tomato Sauce in the bottom and around the sides. '
                 '\n   Layer lasagna sheets on the bottom of the pan, overlapping by 1/2 inch. '
                 '\n   Add one-third of the ricotta and one-quarter of the mozzarella, sausage, pepperoni and Parmesan. '
                 '\n   Spoon 1 cup of tomato sauce over the top. Repeat this two more times.'
                 '\n6. On the top sheet, finish with the remaining cup of tomato sauce, mozzarella, sausage and pepperoni and dust with Parmesan. '
                 '\n   Bake until the cheese bubbles around the edges and the top is melted and light golden brown, about 45 minutes. '
                 "\n   If baking the dish from the freezer, add 15 to 20 minutes to the cook time, or until it's bubbly. "
                 "\n   Cover loosely with foil if it's browning too quickly. "
                 "\n   Remove from the oven; let sit for 15 minutes. "
                 "\n   Cut and serve immediately with more sauce, if desired.")

turkey = Recipe('Turkey Burger',
                '\nINGREDIENTS'
                '\n1 1/2 pounds ground turkey'
                '\n2 poblana peppers, fire-roasted and coarsely diced'
                '\n2 Hatch or Anaheim chiles, fire-roasted and coarsely diced'
                '\n2 garlic cloves, minced'
                '\n 4 green onions (white and light green parts), finely sliced'
                '\nKosher salt and freshly ground black pepper'
                '\n1 tablespoon extra-virgin olive oil'
                '\n4 slices smoked Gouda cheese'
                '\n4 slices pepper Jack cheese'
                '\n4 whole-wheat burger buns'
                '\n1/4 cup roasted garlic butter, melted'
                '\n2 ripe Hass avocados, pitted and peeled'
                '\nJuice of 1 lemon'
                '\nKosher salt and freshly ground black pepper'
                '\n1 heirloom tomato'
                '\n2 tablespoons Donkey Sauce'
                '\n1/4 red onion, thinly sliced'
                '\n1/4 head iceberg lettuce, thinly sliced',
                '\n'
                '\nSTEPS'
                '\n1. To prepare turkey burgers, in a large bowl, combine the turkey, poblanos, Hatch chiles, garlic, and green onions.'
                '\n   Mix until well combined and form into 4 equal balls.'
                '\n   Cover and place in the fridge for 1- minutes to firm up.'
                '\n2. Preheat a large cast-iron griddle or skillet over high heat.'
                '\n3. To cook the burgers, season the burger balls all over with salt and black pepper. '
                '\n   Add a little of the olive oil to the hot griddle. '
                '\n   Place the burger balls on the griddle and cook for 90 seconds to develop a crust.'
                '\n   Using a heavy spatula, smash each burger so it is slightly larger than the size of the bun ((it will shrink back in size as it cooks).'
                '\n   Cook until the underside fo the burger is browned, 3 to 5 minutes.'
                '\n   Flip to another part of the griddle, and cook on the second side for 2 to 3 more minutes.'
                '\n   Top each burger with a slice of smoked Gouda and a slice of pepper Jack cheese.'
                '\n   Cover the burgers with a dome (or an upside-down metal mixing bowl), then lift one side of it quickly and add 23 tablespoons water to the griddle under the dome to steam the burgers and melt the cheese.'
                '\n   Remove the dome and transfer the burgers to a platter to rest.'
                '\n4. Brush the cut sides of the buns lightly with melted garlic butter. Toast the bun halves on the griddle until golden and crisp, about 45 seconds per side.'
                '\n5. In a medium bowl, combine the avocado and lemon juice and season with salt and pepper.'
                '\n   Using a fork, coarsely mash the avocado.'
                '\n   Slice half the heirloom tomato into 54 thin slices and reserve for the burgers.'
                '\n   Dice the rest of the tomato and fold it into the crushed avocado mixture.'
                '\n6. To assemble the burgers, smear the cut sides of the buns with donkey sauce. '
                '\n   Place some sliced red onion on the bottom bun halves and top each with a burger, a tomato slice, a big scoop of crushed avocado, and a large handful of sliced lettuce.'
                '\n   Place the top bun halves on top and serve')

randIndex = random.randrange(len(Recipe.instances))
randFoodChoice = Recipe.instances[randIndex]
payload = 'null'
pick = 'null'
if randFoodChoice.name == mac.name:
    payload = {'content': str(mac.name + mac.ingredients)}
    pick = 'mac'
if randFoodChoice.name == chili.name:
    payload = {'content': str(chili.name + chili.ingredients)}
    pick = 'chili'
if randFoodChoice.name == marsala.name:
    payload = {'content': str(marsala.name + marsala.ingredients)}
    pick = 'marsala'
if randFoodChoice.name == schnitzel.name:
    payload = {'content': str(schnitzel.name + schnitzel.ingredients)}
    pick = 'schnitzel'
if randFoodChoice.name == lasagna.name:
    payload = {'content': str(lasagna.name + lasagna.ingredients)}
    pick = 'lasagna'
if randFoodChoice.name == turkey.name:
    payload = {'content': str(turkey.name + turkey.ingredients)}
    pick = 'turkey'


header = {'authorization': 'MjI1MDg1MDk5OTk2MDg2Mjcy.Gl_y2m.wHfhFWAXvK_MDIG1zR0Llp1bKdHyAWNjhPSNho'}
r = requests.post('https://discord.com/api/v9/channels/979618941162881026/messages', data=payload, headers=header)

if pick == 'mac':
    payload = {'content': str(mac.steps)}
if pick == 'chili':
    payload = {'content': str(chili.steps)}
if pick == 'marsala':
    payload = {'content': str(marsala.steps)}
if pick == 'schnitzel':
    payload = {'content': str(schnitzel.steps)}
if pick == 'lasagna':
    payload = {'content': str(lasagna.steps)}
if pick == 'turkey':
    payload = {'content': str(turkey.steps)}

r = requests.post('https://discord.com/api/v9/channels/979618941162881026/messages', data=payload, headers=header)
print(str(payload))
