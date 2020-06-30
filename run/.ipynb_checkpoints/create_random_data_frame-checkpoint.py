#!/usr/bin/env python

from src.randomdata import RandomFrame

def main(): 
    
    frame_engine = RandomFrame(1, 1000, 5, 10)
    df = frame_engine.generate_frame()
    df.to_csv('data/random_frame.csv', index=False)

if __name__ == '__main__':
    main()