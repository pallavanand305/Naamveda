"""
Numerology Engine for Naamveda
Calculates destiny numbers, compatibility scores, and lucky traits
"""

from typing import Dict, List
from datetime import datetime

class NumerologyEngine:
    """Advanced numerology calculations for Indian baby names"""
    
    # Chaldean System (Primary for Indian names)
    CHALDEAN_MAP = {
        'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,
        'B': 2, 'K': 2, 'R': 2,
        'C': 3, 'G': 3, 'L': 3, 'S': 3,
        'D': 4, 'M': 4, 'T': 4,
        'E': 5, 'H': 5, 'N': 5, 'X': 5,
        'U': 6, 'V': 6, 'W': 6,
        'O': 7, 'Z': 7,
        'F': 8, 'P': 8
    }
    
    # Number meanings with Indian spiritual context
    NUMBER_MEANINGS = {
        1: {
            'trait': 'Leader, Independent, Ambitious',
            'emotion': 'Your child will be a natural-born leader with strong willpower',
            'career': 'Entrepreneur, CEO, Politician, Innovator',
            'lucky_day': 'Sunday',
            'lucky_color': 'Red, Orange, Gold',
            'planet': 'Sun (Surya)',
            'deity': 'Lord Brahma',
            'spiritual': 'Represents new beginnings and divine creation'
        },
        2: {
            'trait': 'Diplomatic, Sensitive, Cooperative',
            'emotion': 'Your child will be a peacemaker with emotional intelligence',
            'career': 'Counselor, Diplomat, Artist, Healer',
            'lucky_day': 'Monday',
            'lucky_color': 'White, Cream, Silver',
            'planet': 'Moon (Chandra)',
            'deity': 'Goddess Parvati',
            'spiritual': 'Represents duality and balance'
        },
        3: {
            'trait': 'Creative, Expressive, Joyful',
            'emotion': 'Your child will spread happiness and inspire others',
            'career': 'Writer, Performer, Teacher, Designer',
            'lucky_day': 'Thursday',
            'lucky_color': 'Yellow, Purple, Violet',
            'planet': 'Jupiter (Guru)',
            'deity': 'Lord Vishnu',
            'spiritual': 'Represents wisdom and expansion'
        },
        4: {
            'trait': 'Practical, Hardworking, Stable',
            'emotion': 'Your child will be dependable and build strong foundations',
            'career': 'Engineer, Architect, Manager, Builder',
            'lucky_day': 'Sunday, Saturday',
            'lucky_color': 'Blue, Grey, Khaki',
            'planet': 'Rahu',
            'deity': 'Lord Ganesha',
            'spiritual': 'Represents stability and material success'
        },
        5: {
            'trait': 'Adventurous, Dynamic, Freedom-loving',
            'emotion': 'Your child will explore the world with curiosity',
            'career': 'Traveler, Marketer, Journalist, Entrepreneur',
            'lucky_day': 'Wednesday',
            'lucky_color': 'Green, Light Blue, Turquoise',
            'planet': 'Mercury (Budh)',
            'deity': 'Lord Hanuman',
            'spiritual': 'Represents change and versatility'
        },
        6: {
            'trait': 'Nurturing, Responsible, Harmonious',
            'emotion': 'Your child will care for others with compassion',
            'career': 'Teacher, Doctor, Social Worker, Chef',
            'lucky_day': 'Friday',
            'lucky_color': 'Pink, Blue, White',
            'planet': 'Venus (Shukra)',
            'deity': 'Goddess Lakshmi',
            'spiritual': 'Represents love and harmony'
        },
        7: {
            'trait': 'Spiritual, Analytical, Wise',
            'emotion': 'Your child will seek deeper truths and enlightenment',
            'career': 'Researcher, Philosopher, Healer, Scientist',
            'lucky_day': 'Monday',
            'lucky_color': 'Violet, Purple, Lavender',
            'planet': 'Ketu',
            'deity': 'Lord Shiva',
            'spiritual': 'Represents spirituality and mysticism'
        },
        8: {
            'trait': 'Powerful, Ambitious, Successful',
            'emotion': 'Your child will achieve greatness through determination',
            'career': 'Business Leader, Banker, Judge, Politician',
            'lucky_day': 'Saturday',
            'lucky_color': 'Black, Dark Blue, Purple',
            'planet': 'Saturn (Shani)',
            'deity': 'Lord Yama',
            'spiritual': 'Represents karma and discipline'
        },
        9: {
            'trait': 'Compassionate, Humanitarian, Wise',
            'emotion': 'Your child will change the world with kindness',
            'career': 'Activist, Healer, Spiritual Leader, Philanthropist',
            'lucky_day': 'Tuesday',
            'lucky_color': 'Red, Maroon, Crimson',
            'planet': 'Mars (Mangal)',
            'deity': 'Lord Hanuman',
            'spiritual': 'Represents completion and universal love'
        },
        11: {
            'trait': 'Intuitive, Inspirational, Visionary',
            'emotion': 'Your child is a master number - destined for spiritual leadership',
            'career': 'Spiritual Teacher, Inventor, Artist, Visionary',
            'lucky_day': 'Monday, Thursday',
            'lucky_color': 'Silver, White, Gold',
            'planet': 'Moon + Jupiter',
            'deity': 'Lord Krishna',
            'spiritual': 'Master number - represents enlightenment'
        },
        22: {
            'trait': 'Master Builder, Practical Visionary',
            'emotion': 'Your child will manifest grand visions into reality',
            'career': 'Architect, Engineer, Global Leader, Innovator',
            'lucky_day': 'All days',
            'lucky_color': 'All colors',
            'planet': 'All planets',
            'deity': 'Lord Vishwakarma',
            'spiritual': 'Master number - represents material mastery'
        },
        33: {
            'trait': 'Master Teacher, Healer, Compassionate Leader',
            'emotion': 'Your child will uplift humanity through service',
            'career': 'Spiritual Teacher, Healer, Humanitarian Leader',
            'lucky_day': 'All days',
            'lucky_color': 'Gold, White, Saffron',
            'planet': 'All planets',
            'deity': 'Lord Buddha',
            'spiritual': 'Master number - represents universal compassion'
        }
    }
    
    @staticmethod
    def reduce_to_single_digit(number: int) -> int:
        """Reduce to single digit, preserving master numbers"""
        while number > 9 and number not in [11, 22, 33]:
            number = sum(int(digit) for digit in str(number))
        return number
    
    @classmethod
    def calculate_name_number(cls, name: str) -> int:
        """Calculate name number using Chaldean system"""
        name = name.upper().replace(' ', '')
        total = sum(cls.CHALDEAN_MAP.get(char, 0) for char in name if char.isalpha())
        return cls.reduce_to_single_digit(total)
    
    @classmethod
    def calculate_destiny_number(cls, full_name: str) -> int:
        """Calculate destiny number from full name"""
        return cls.calculate_name_number(full_name)
    
    @classmethod
    def calculate_soul_number(cls, name: str) -> int:
        """Calculate soul number from vowels"""
        vowels = ''.join(char for char in name.upper() if char in 'AEIOU')
        return cls.calculate_name_number(vowels)
    
    @classmethod
    def calculate_personality_number(cls, name: str) -> int:
        """Calculate personality number from consonants"""
        consonants = ''.join(char for char in name.upper() if char.isalpha() and char not in 'AEIOU')
        return cls.calculate_name_number(consonants)
    
    @classmethod
    def calculate_life_path_number(cls, dob: datetime) -> int:
        """Calculate life path number from date of birth"""
        day = dob.day
        month = dob.month
        year = dob.year
        
        total = sum(int(d) for d in str(day) + str(month) + str(year))
        return cls.reduce_to_single_digit(total)
    
    @classmethod
    def calculate_compatibility_score(cls, name_number: int, life_path: int) -> int:
        """Calculate compatibility between name and life path (0-100)"""
        # Compatible pairs
        compatible = [
            (1, 5), (1, 7), (2, 6), (2, 8), (3, 6), (3, 9),
            (4, 8), (5, 7), (6, 9), (7, 9), (1, 1), (2, 2),
            (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)
        ]
        
        # Master numbers always score high
        if name_number in [11, 22, 33] or life_path in [11, 22, 33]:
            return 95
        
        if name_number == life_path:
            return 100
        elif (name_number, life_path) in compatible or (life_path, name_number) in compatible:
            return 85
        else:
            return 70
    
    @classmethod
    def get_complete_analysis(cls, name: str, dob: datetime = None) -> Dict:
        """Get complete numerology analysis"""
        destiny = cls.calculate_destiny_number(name)
        soul = cls.calculate_soul_number(name)
        personality = cls.calculate_personality_number(name)
        
        analysis = {
            'name': name,
            'destiny_number': destiny,
            'soul_number': soul,
            'personality_number': personality,
            'destiny_meaning': cls.NUMBER_MEANINGS.get(destiny, {}),
            'soul_meaning': cls.NUMBER_MEANINGS.get(soul, {}),
            'personality_meaning': cls.NUMBER_MEANINGS.get(personality, {}),
        }
        
        if dob:
            life_path = cls.calculate_life_path_number(dob)
            compatibility = cls.calculate_compatibility_score(destiny, life_path)
            
            analysis.update({
                'life_path_number': life_path,
                'life_path_meaning': cls.NUMBER_MEANINGS.get(life_path, {}),
                'compatibility_score': compatibility,
                'compatibility_text': cls._get_compatibility_text(compatibility)
            })
        
        return analysis
    
    @staticmethod
    def _get_compatibility_text(score: int) -> str:
        """Get compatibility description"""
        if score >= 95:
            return "Perfect Match - Highly Auspicious"
        elif score >= 85:
            return "Excellent Compatibility"
        elif score >= 70:
            return "Good Harmony"
        else:
            return "Neutral"
    
    @classmethod
    def is_name_auspicious(cls, name: str, dob: datetime = None) -> bool:
        """Check if name is auspicious"""
        analysis = cls.get_complete_analysis(name, dob)
        
        # Master numbers are always auspicious
        if analysis['destiny_number'] in [11, 22, 33]:
            return True
        
        # High compatibility score
        if dob and analysis.get('compatibility_score', 0) >= 85:
            return True
        
        # Favorable destiny numbers
        if analysis['destiny_number'] in [1, 3, 5, 6, 9]:
            return True
        
        return False
