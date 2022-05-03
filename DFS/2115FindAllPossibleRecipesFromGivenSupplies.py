# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
class Solution:
    # time complexity: O(N*k)
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        self.supplies = set(supplies)
        self.recipes = {r:idx for idx,r in enumerate(recipes)}
        triedRecipes = {}
        
        def createRecipe(idx,parents): # circle?
            if recipes[idx] in triedRecipes:
                return triedRecipes[recipes[idx]]
            for i, ingredient in enumerate(ingredients[idx]):
                if ingredient in self.supplies:
                    continue
                elif ingredient in self.recipes:
                    if ingredient in parents:
                        triedRecipes[recipes[idx]] = False
                        return False
                    parents.add(recipes[idx])
                    if not createRecipe(self.recipes[ingredient], parents):
                        triedRecipes[recipes[idx]] = False
                        return False
                else: # not in suppliers and not in recipes
                    # print('else')
                    triedRecipes[recipes[idx]] = False
                    return False
            triedRecipes[recipes[idx]] = True
            return True
                    
        
        
        for idx, _ in enumerate(recipes):
            createRecipe(idx,set())
        return [key for key,val in triedRecipes.items() if val]    
            
        