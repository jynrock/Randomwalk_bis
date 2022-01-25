from randomwalk.random_walk import*

if __name__ == '__main__':
    game = random_walk()
    game.boundaries("walls")
    game.set_custom_slate(extent=(100, 100))
    game.add_pattern(name="glider_gun",upper_corner=(30, 30))
    game.run_plot(steps=1000)