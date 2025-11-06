class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        # Two asteroids will collide if the left is positve and right is negative
        # if first is negative and second is positive they wont collide

        for value in asteroids:
            destroyed = False  # flag to check if current asteroid is destroyed or not
            while st and st[-1] > 0 and value < 0:
                if abs(value) > abs(st[-1]):
                    st.pop()
                    continue
                elif abs(value) == abs(st[-1]):
                    st.pop()
                destroyed = True
                break
            
            if not destroyed:
                st.append(value)

        return st