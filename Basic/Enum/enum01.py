"""
    পাইথনে Enum (Enumeration) হলো এমন একটি বিশেষ ক্লাস যার মাধ্যমে আপনি এক সেট নির্দিষ্ট বা ধ্রুবক (Constant) 
    মানকে একটি অর্থপূর্ণ নাম দিয়ে গ্রুপ করে রাখতে পারেন।

    সহজ ভাষায়, যখন আপনার প্রজেক্টে এমন কিছু মান থাকে যা কখনো পরিবর্তন হবে না (যেমন: সপ্তাহের সাত দিন, দিক—উত্তর, 
    দক্ষিণ, পূর্ব, পশ্চিম), তখন সেগুলো আলাদা আলাদা ভেরিয়েবলে না রেখে Enum ব্যবহার করা বেশি বুদ্ধিমান।
"""

from enum import Enum

class RobotDirection(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


current_direction = RobotDirection.NORTH

if current_direction == RobotDirection.NORTH:
    print("Robort gone on north side.")