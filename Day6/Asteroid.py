def asteroid_collision(asteroids):
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            top = stack[-1]
            if top < -asteroid:
                stack.pop()
                continue
            elif top == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    
    if not stack:
        return "Everything Destroyed"
    
    return stack
