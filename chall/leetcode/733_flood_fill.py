class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def help(image, old, new, x, y):
            if not (0 <= x < len(image) and 0 <= y < len(image[0])):
                return
            if image[x][y] != old:
                return
            image[x][y] = new
            help(image, old, new, x+1, y)
            help(image, old, new, x-1, y)
            help(image, old, new, x, y+1)
            help(image, old, new, x, y-1)
        old_color = image[sr][sc]
        if old_color != color:
            help(image, old_color, color, sr, sc)
        return image
