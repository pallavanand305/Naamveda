"""
AI Name Generator using OpenAI
Generates culturally authentic Indian baby names
"""

from typing import List, Dict
from openai import OpenAI
from app.core.config import settings
from app.services.numerology import NumerologyEngine
from datetime import datetime
import json

class AINameGenerator:
    """AI-powered Indian baby name generator"""
    
    def __init__(self):
        # Check if OpenAI key is valid (not a dummy/test key)
        dummy_keys = [
            "sk-your-key-here-replace-this",
            "sk-dummy-key-for-testing",
            "sk-test",
            "your-openai-key-here"
        ]
        
        has_valid_key = (
            settings.OPENAI_API_KEY and 
            settings.OPENAI_API_KEY not in dummy_keys and
            settings.OPENAI_API_KEY.startswith("sk-") and
            len(settings.OPENAI_API_KEY) > 20
        )
        
        if has_valid_key:
            self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
            self.use_ai = True
        else:
            self.client = None
            self.use_ai = False
        
        self.numerology = NumerologyEngine()
    
    def generate_names(
        self,
        gender: str,
        dob: datetime,
        starting_letter: str = None,
        religion: str = "Hindu",
        style: str = "Modern",
        emotional_intention: str = "Success",
        nakshatra: str = None,
        count: int = 10
    ) -> List[Dict]:
        """
        Generate AI-powered baby names
        
        Args:
            gender: Male/Female/Unisex
            dob: Date of birth
            starting_letter: Preferred starting letter
            religion: Hindu/Sikh/Jain/Buddhist
            style: Modern/Traditional/Unique
            emotional_intention: Success/Peace/Devotion/Prosperity/Wisdom/Strength
            nakshatra: Birth nakshatra (optional)
            count: Number of names to generate
        
        Returns:
            List of name dictionaries with meanings and numerology
        """
        
        # Calculate life path number
        life_path = self.numerology.calculate_life_path_number(dob)
        
        # If OpenAI is not available, use mock data
        if not self.use_ai:
            return self._generate_mock_names(
                gender=gender,
                life_path=life_path,
                starting_letter=starting_letter,
                emotional_intention=emotional_intention,
                count=count
            )
        
        # Build AI prompt
        prompt = self._build_prompt(
            gender=gender,
            life_path=life_path,
            starting_letter=starting_letter,
            religion=religion,
            style=style,
            emotional_intention=emotional_intention,
            nakshatra=nakshatra,
            count=count
        )
        
        # Call OpenAI
        response = self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in Indian baby names, Sanskrit etymology, numerology, and Vedic astrology. Generate authentic, meaningful names with deep cultural significance."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8,
            max_tokens=2000,
            response_format={"type": "json_object"}
        )
        
        # Parse response
        names_data = json.loads(response.choices[0].message.content)
        
        # Enhance with numerology
        enhanced_names = []
        for name_data in names_data.get('names', []):
            name = name_data['name']
            
            # Calculate numerology
            numerology_analysis = self.numerology.get_complete_analysis(name, dob)
            
            enhanced_names.append({
                'name': name,
                'meaning': name_data['meaning'],
                'sanskrit_origin': name_data.get('sanskrit_origin', ''),
                'cultural_significance': name_data.get('cultural_significance', ''),
                'destiny_number': numerology_analysis['destiny_number'],
                'soul_number': numerology_analysis['soul_number'],
                'personality_number': numerology_analysis['personality_number'],
                'life_path_number': numerology_analysis.get('life_path_number'),
                'compatibility_score': numerology_analysis.get('compatibility_score', 0),
                'lucky_traits': numerology_analysis['destiny_meaning'],
                'spiritual_blessing': self._generate_blessing(name, emotional_intention),
                'why_this_name': name_data.get('why_this_name', ''),
                'is_auspicious': self.numerology.is_name_auspicious(name, dob)
            })
        
        # Sort by compatibility score
        enhanced_names.sort(key=lambda x: x['compatibility_score'], reverse=True)
        
        return enhanced_names[:count]
    
    def _build_prompt(
        self,
        gender: str,
        life_path: int,
        starting_letter: str,
        religion: str,
        style: str,
        emotional_intention: str,
        nakshatra: str,
        count: int
    ) -> str:
        """Build AI prompt for name generation"""
        
        prompt = f"""Generate {count} authentic Indian baby names with the following criteria:

**Requirements:**
- Gender: {gender}
- Life Path Number: {life_path} (numerology)
- Religion/Culture: {religion}
- Style: {style}
- Emotional Intention: {emotional_intention}
"""
        
        if starting_letter:
            prompt += f"- Must start with letter: {starting_letter}\n"
        
        if nakshatra:
            prompt += f"- Birth Nakshatra: {nakshatra}\n"
        
        prompt += f"""
**Instructions:**
1. Each name should be culturally authentic and meaningful
2. Provide Sanskrit/Hindi origin and deep meaning
3. Explain why this name suits the child's numerology (Life Path {life_path})
4. Connect the name to the emotional intention: {emotional_intention}
5. Include cultural/spiritual significance
6. Names should be pronounceable and {style.lower()} in style

**Output Format (JSON):**
{{
    "names": [
        {{
            "name": "Name in English",
            "meaning": "Deep meaning in English",
            "sanskrit_origin": "Sanskrit/Hindi origin word",
            "cultural_significance": "Cultural or mythological significance",
            "why_this_name": "Why this name is perfect for a child with Life Path {life_path} seeking {emotional_intention}"
        }}
    ]
}}

Generate names that parents will emotionally connect with. Make each name special and meaningful.
"""
        
        return prompt
    
    def _generate_blessing(self, name: str, intention: str) -> str:
        """Generate spiritual blessing message"""
        blessings = {
            "Success": f"May {name} achieve great success and prosperity in all endeavors. May every path lead to victory.",
            "Peace": f"May {name} find inner peace and spread tranquility wherever they go. Om Shanti.",
            "Devotion": f"May {name} walk the path of devotion and find divine grace in every moment.",
            "Prosperity": f"May {name} be blessed with abundance, wealth, and prosperity. May Goddess Lakshmi shower her blessings.",
            "Wisdom": f"May {name} be blessed with wisdom and knowledge. May Goddess Saraswati guide their path.",
            "Strength": f"May {name} have the strength of Lord Hanuman and courage to overcome all obstacles."
        }
        
        return blessings.get(intention, f"May {name} be blessed with happiness, health, and success.")
    
    def _generate_mock_names(
        self,
        gender: str,
        life_path: int,
        starting_letter: str = None,
        emotional_intention: str = "Success",
        count: int = 10
    ) -> List[Dict]:
        """
        Generate mock names when OpenAI is not available
        Uses pre-defined Indian names with real numerology
        """
        
        # Pre-defined Indian names database (30+ names for better variety)
        male_names = [
            # Modern & Popular
            {"name": "Aarav", "meaning": "Peaceful, Calm", "origin": "Sanskrit"},
            {"name": "Arjun", "meaning": "Bright, Shining, White", "origin": "Sanskrit"},
            {"name": "Vihaan", "meaning": "Dawn, Morning", "origin": "Sanskrit"},
            {"name": "Aditya", "meaning": "Sun, Lord Surya", "origin": "Sanskrit"},
            {"name": "Reyansh", "meaning": "Ray of Light", "origin": "Sanskrit"},
            {"name": "Ayaan", "meaning": "Gift of God", "origin": "Sanskrit"},
            {"name": "Advait", "meaning": "Unique, One", "origin": "Sanskrit"},
            {"name": "Vivaan", "meaning": "Full of Life", "origin": "Sanskrit"},
            {"name": "Atharv", "meaning": "Lord Ganesh, Knowledgeable", "origin": "Sanskrit"},
            {"name": "Sai", "meaning": "Divine, Sai Baba", "origin": "Sanskrit"},
            # Traditional & Spiritual
            {"name": "Krishna", "meaning": "Dark, Lord Krishna", "origin": "Sanskrit"},
            {"name": "Shaurya", "meaning": "Bravery, Courage", "origin": "Sanskrit"},
            {"name": "Rudra", "meaning": "Lord Shiva", "origin": "Sanskrit"},
            {"name": "Dhruv", "meaning": "Pole Star, Constant", "origin": "Sanskrit"},
            {"name": "Arnav", "meaning": "Ocean, Sea", "origin": "Sanskrit"},
            {"name": "Shivansh", "meaning": "Part of Lord Shiva", "origin": "Sanskrit"},
            {"name": "Vedant", "meaning": "Ultimate Wisdom", "origin": "Sanskrit"},
            {"name": "Aarush", "meaning": "First Ray of Sun", "origin": "Sanskrit"},
            {"name": "Kabir", "meaning": "Great, Powerful", "origin": "Sanskrit"},
            {"name": "Yash", "meaning": "Success, Fame", "origin": "Sanskrit"},
        ]
        
        female_names = [
            # Modern & Popular
            {"name": "Ananya", "meaning": "Unique, Incomparable", "origin": "Sanskrit"},
            {"name": "Aadhya", "meaning": "First Power, Goddess Durga", "origin": "Sanskrit"},
            {"name": "Diya", "meaning": "Lamp, Light", "origin": "Sanskrit"},
            {"name": "Saanvi", "meaning": "Goddess Lakshmi", "origin": "Sanskrit"},
            {"name": "Anika", "meaning": "Grace, Favor", "origin": "Sanskrit"},
            {"name": "Ishita", "meaning": "Desired, Superior", "origin": "Sanskrit"},
            {"name": "Navya", "meaning": "New, Young", "origin": "Sanskrit"},
            {"name": "Myra", "meaning": "Sweet, Beloved", "origin": "Sanskrit"},
            {"name": "Kiara", "meaning": "Dark-haired, Pure", "origin": "Sanskrit"},
            {"name": "Avni", "meaning": "Earth", "origin": "Sanskrit"},
            # Traditional & Spiritual
            {"name": "Aaradhya", "meaning": "Worshipped, Blessed", "origin": "Sanskrit"},
            {"name": "Siya", "meaning": "Goddess Sita", "origin": "Sanskrit"},
            {"name": "Pari", "meaning": "Fairy, Angel", "origin": "Sanskrit"},
            {"name": "Riya", "meaning": "Singer, Graceful", "origin": "Sanskrit"},
            {"name": "Shanaya", "meaning": "First Ray of Sun", "origin": "Sanskrit"},
            {"name": "Anvi", "meaning": "Goddess of Forest", "origin": "Sanskrit"},
            {"name": "Ira", "meaning": "Earth, Goddess Saraswati", "origin": "Sanskrit"},
            {"name": "Kavya", "meaning": "Poetry, Poem", "origin": "Sanskrit"},
            {"name": "Prisha", "meaning": "Beloved, God's Gift", "origin": "Sanskrit"},
            {"name": "Zara", "meaning": "Princess, Flower", "origin": "Sanskrit"},
        ]
        
        unisex_names = [
            {"name": "Arya", "meaning": "Noble, Honorable", "origin": "Sanskrit"},
            {"name": "Amar", "meaning": "Immortal, Eternal", "origin": "Sanskrit"},
            {"name": "Divya", "meaning": "Divine, Heavenly", "origin": "Sanskrit"},
            {"name": "Avi", "meaning": "Sun and Air", "origin": "Sanskrit"},
            {"name": "Daksh", "meaning": "Capable, Talented", "origin": "Sanskrit"},
        ]
        
        # Select names based on gender
        if gender.lower() == "male":
            name_pool = male_names
        elif gender.lower() == "female":
            name_pool = female_names
        else:
            name_pool = male_names + female_names + unisex_names
        
        # Filter by starting letter if provided
        if starting_letter:
            filtered = [n for n in name_pool if n['name'][0].upper() == starting_letter.upper()]
            if filtered:
                name_pool = filtered
        
        # Generate names with numerology
        enhanced_names = []
        for name_data in name_pool[:count]:
            name = name_data['name']
            
            # Calculate numerology
            from datetime import datetime
            dob = datetime.now()  # Use current date for mock
            numerology_analysis = self.numerology.get_complete_analysis(name, dob)
            
            # Create why_this_name based on emotional intention
            why_texts = {
                "Success": f"{name} carries the vibration of achievement and ambition. This name will inspire your child to reach great heights and succeed in all endeavors.",
                "Peace": f"{name} resonates with tranquility and harmony. This name will bring calmness and serenity to your child's life.",
                "Devotion": f"{name} embodies spiritual connection and divine grace. This name will guide your child on a path of devotion and faith.",
                "Prosperity": f"{name} attracts abundance and wealth. This name will open doors of prosperity for your child.",
                "Wisdom": f"{name} channels knowledge and understanding. This name will bless your child with wisdom beyond their years.",
                "Strength": f"{name} represents power and courage. This name will give your child the strength to overcome any obstacle."
            }
            
            enhanced_names.append({
                'name': name,
                'meaning': name_data['meaning'],
                'sanskrit_origin': name_data['origin'],
                'cultural_significance': f"A popular and auspicious name in Indian culture, {name} has been cherished for generations.",
                'destiny_number': numerology_analysis['destiny_number'],
                'soul_number': numerology_analysis['soul_number'],
                'personality_number': numerology_analysis['personality_number'],
                'life_path_number': numerology_analysis.get('life_path_number'),
                'compatibility_score': numerology_analysis.get('compatibility_score', 85),
                'lucky_traits': numerology_analysis['destiny_meaning'],
                'spiritual_blessing': self._generate_blessing(name, emotional_intention),
                'why_this_name': why_texts.get(emotional_intention, f"{name} is a beautiful choice that will bring joy and success to your child."),
                'is_auspicious': self.numerology.is_name_auspicious(name, dob)
            })
        
        # Sort by compatibility score
        enhanced_names.sort(key=lambda x: x['compatibility_score'], reverse=True)
        
        return enhanced_names[:count]
    
    def generate_preview(
        self,
        gender: str,
        dob: datetime,
        starting_letter: str = None,
        religion: str = "Hindu",
        style: str = "Modern",
        emotional_intention: str = "Success"
    ) -> List[Dict]:
        """Generate free preview (3 names)"""
        return self.generate_names(
            gender=gender,
            dob=dob,
            starting_letter=starting_letter,
            religion=religion,
            style=style,
            emotional_intention=emotional_intention,
            count=settings.FREE_NAMES_COUNT
        )
    
    def generate_premium(
        self,
        gender: str,
        dob: datetime,
        time_of_birth: str = None,
        nakshatra: str = None,
        starting_letter: str = None,
        religion: str = "Hindu",
        style: str = "Modern",
        emotional_intention: str = "Success"
    ) -> List[Dict]:
        """Generate premium report (10 names)"""
        return self.generate_names(
            gender=gender,
            dob=dob,
            starting_letter=starting_letter,
            religion=religion,
            style=style,
            emotional_intention=emotional_intention,
            nakshatra=nakshatra,
            count=settings.PREMIUM_NAMES_COUNT
        )
