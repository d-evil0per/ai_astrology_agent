#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Interpretation Generation Module"""

# --- Interpretation Texts ---
# These are comprehensive interpretations for planets in signs, planets in houses,
# aspects between planets, and house cusp signs.

PLANET_IN_SIGN_INTERPRETATIONS = {
    "Sun": {
        "Aries": "Sun in Aries signifies a pioneering spirit, courage, and a direct approach to life. You are likely energetic and assertive.",
        "Taurus": "Sun in Taurus indicates a love for stability, beauty, and the material world. You are likely patient and determined.",
        "Gemini": "Sun in Gemini indicates a curious, communicative, and adaptable nature. You are likely versatile and enjoy learning and sharing ideas.",
        "Cancer": "Sun in Cancer suggests a nurturing, protective, and emotional core. You are likely intuitive and value home and family.",
        "Leo": "Sun in Leo signifies a strong need for self-expression, creativity, and recognition. You are likely confident and charismatic.",
        "Virgo": "Sun in Virgo points to a practical, analytical, and service-oriented approach to life. You are likely detail-oriented and strive for perfection.",
        "Libra": "Sun in Libra indicates a focus on relationships, harmony, and balance. You are likely diplomatic and value fairness.",
        "Scorpio": "Sun in Scorpio suggests intensity, depth, and a desire for transformation. You are likely passionate and resourceful.",
        "Sagittarius": "Sun in Sagittarius signifies a love for adventure, freedom, and philosophical pursuits. You are likely optimistic and enthusiastic.",
        "Capricorn": "Sun in Capricorn indicates ambition, discipline, and a strong sense of responsibility. You are likely practical and goal-oriented.",
        "Aquarius": "Sun in Aquarius suggests a focus on innovation, individuality, and humanitarian ideals. You are likely original and progressive.",
        "Pisces": "Sun in Pisces suggests a compassionate, imaginative, and sensitive nature. You are likely intuitive and artistic."
    },
    "Moon": {
        "Aries": "Moon in Aries points to quick emotional responses and a need for independence in emotional expression.",
        "Taurus": "Moon in Taurus seeks emotional security through comfort and stability. You likely have a calm and steady emotional nature.",
        "Gemini": "Moon in Gemini indicates a need for variety and mental stimulation in emotional matters. You likely have a quick wit and enjoy communication.",
        "Cancer": "Moon in Cancer suggests deep emotional sensitivity and a strong attachment to home and family. You are likely nurturing and protective.",
        "Leo": "Moon in Leo points to a need for recognition and creative expression in emotional fulfillment. You likely have a warm and generous nature.",
        "Virgo": "Moon in Virgo indicates a practical and analytical approach to emotions. You likely seek order and are helpful to others.",
        "Libra": "Moon in Libra suggests a need for harmony and balance in relationships. You likely have a diplomatic and charming demeanor.",
        "Scorpio": "Moon in Scorpio indicates intense emotions and a desire for deep connections. You likely have strong intuition and are not afraid of the darker aspects of life.",
        "Sagittarius": "Moon in Sagittarius points to a need for freedom and adventure in emotional expression. You likely have an optimistic and philosophical outlook.",
        "Capricorn": "Moon in Capricorn suggests a reserved and disciplined emotional nature. You likely value tradition and have a strong sense of duty.",
        "Aquarius": "Moon in Aquarius indicates a need for independence and originality in emotional matters. You likely have a progressive and humanitarian spirit.",
        "Pisces": "Moon in Pisces indicates deep empathy, a rich inner world, and a highly sensitive emotional nature."
    },
    "Mercury": {
        "Aries": "Mercury in Aries indicates a quick, direct, and assertive communication style. You likely think and speak with enthusiasm and courage.",
        "Taurus": "Mercury in Taurus suggests a practical, deliberate, and sensual way of thinking and communicating. You likely value stability and are thorough in your thoughts.",
        "Gemini": "Mercury in Gemini points to a curious, versatile, and communicative mind. You likely enjoy learning and sharing information.",
        "Cancer": "Mercury in Cancer indicates an intuitive and emotional approach to thinking and communicating. You likely have a good memory and are sensitive to others' feelings.",
        "Leo": "Mercury in Leo suggests a dramatic, confident, and creative communication style. You likely express yourself with flair and enjoy being the center of attention.",
        "Virgo": "Mercury in Virgo indicates a precise, analytical, and detail-oriented mind. You likely excel at problem-solving and critical thinking.",
        "Libra": "Mercury in Libra points to a diplomatic, balanced, and relationship-focused way of thinking and communicating. You likely seek harmony and fairness in discussions.",
        "Scorpio": "Mercury in Scorpio suggests a deep, investigative, and intense approach to thinking and communicating. You likely have a penetrating mind and are not afraid to explore taboo subjects.",
        "Sagittarius": "Mercury in Sagittarius indicates a broad-minded, optimistic, and philosophical way of thinking and communicating. You likely enjoy exploring new ideas and cultures.",
        "Capricorn": "Mercury in Capricorn suggests a practical, disciplined, and structured approach to thinking and communicating. You likely value tradition and have a strategic mind.",
        "Aquarius": "Mercury in Aquarius points to an innovative, original, and unconventional way of thinking and communicating. You likely have a progressive and humanitarian outlook.",
        "Pisces": "Mercury in Pisces indicates an intuitive, imaginative, and empathetic approach to thinking and communicating. You likely have a poetic and artistic mind."
    },
    "Venus": {
        "Aries": "Venus in Aries indicates a passionate, impulsive, and direct approach to love and relationships. You likely enjoy the thrill of the chase and are attracted to excitement.",
        "Taurus": "Venus in Taurus suggests a sensual, loyal, and stable approach to love and relationships. You likely value comfort, beauty, and material security.",
        "Gemini": "Venus in Gemini points to a curious, communicative, and playful approach to love and relationships. You likely enjoy intellectual stimulation and variety.",
        "Cancer": "Venus in Cancer indicates a nurturing, protective, and emotional approach to love and relationships. You likely value home, family, and emotional security.",
        "Leo": "Venus in Leo suggests a warm, generous, and dramatic approach to love and relationships. You likely enjoy romance, creativity, and being admired.",
        "Virgo": "Venus in Virgo points to a practical, analytical, and service-oriented approach to love and relationships. You likely express love through acts of service and attention to detail.",
        "Libra": "Venus in Libra indicates a harmonious, balanced, and relationship-focused approach to love and relationships. You likely value fairness, beauty, and partnership.",
        "Scorpio": "Venus in Scorpio suggests an intense, passionate, and transformative approach to love and relationships. You likely seek deep emotional connections and are not afraid of intimacy.",
        "Sagittarius": "Venus in Sagittarius points to an adventurous, optimistic, and freedom-loving approach to love and relationships. You likely enjoy exploring new cultures and philosophies with your partner.",
        "Capricorn": "Venus in Capricorn indicates a serious, committed, and traditional approach to love and relationships. You likely value stability, responsibility, and long-term goals.",
        "Aquarius": "Venus in Aquarius suggests an unconventional, independent, and progressive approach to love and relationships. You likely value friendship, intellectual connection, and individuality.",
        "Pisces": "Venus in Pisces points to a compassionate, romantic, and dreamy approach to love and relationships. You likely have a strong sense of empathy and are attracted to the mystical."
    },
    "Mars": {
        "Aries": "Mars in Aries indicates a strong, direct, and courageous approach to action and conflict. You are likely assertive and enjoy taking the initiative.",
        "Taurus": "Mars in Taurus suggests a steady, determined, and persistent approach to achieving goals. You likely value security and are patient in your pursuits.",
        "Gemini": "Mars in Gemini points to a versatile, communicative, and intellectually driven approach to action. You likely enjoy multitasking and mental challenges.",
        "Cancer": "Mars in Cancer indicates an emotional, protective, and nurturing approach to action and conflict. You likely defend your loved ones fiercely.",
        "Leo": "Mars in Leo suggests a confident, creative, and dramatic approach to action. You likely seek recognition and enjoy expressing yourself boldly.",
        "Virgo": "Mars in Virgo points to a precise, analytical, and service-oriented approach to action. You likely excel at detailed work and strive for efficiency.",
        "Libra": "Mars in Libra indicates a diplomatic, balanced, and relationship-focused approach to action and conflict. You likely seek harmony and fairness in your endeavors.",
        "Scorpio": "Mars in Scorpio provides intense drive, resourcefulness, and a desire to delve deep beneath the surface. Your actions are powerful and transformative.",
        "Sagittarius": "Mars in Sagittarius suggests an adventurous, optimistic, and freedom-loving approach to action. You likely enjoy exploring new horizons and taking risks.",
        "Capricorn": "Mars in Capricorn indicates a disciplined, ambitious, and strategic approach to achieving goals. You likely value structure and long-term success.",
        "Aquarius": "Mars in Aquarius points to an innovative, independent, and unconventional approach to action. You likely value individuality and humanitarian causes.",
        "Pisces": "Mars in Pisces suggests a compassionate, intuitive, and imaginative approach to action. You likely act on your ideals and are drawn to artistic or spiritual pursuits."
    },
    "Jupiter": {
        "Aries": "Jupiter in Aries indicates a bold, pioneering, and enthusiastic approach to growth and expansion. You likely seek new opportunities with courage and optimism.",
        "Taurus": "Jupiter in Taurus suggests a steady, patient, and value-driven approach to growth. You likely find abundance through persistence and appreciation of beauty.",
        "Gemini": "Jupiter in Gemini points to a curious, communicative, and versatile approach to learning and expansion. You likely enjoy exploring diverse ideas and sharing knowledge.",
        "Cancer": "Jupiter in Cancer indicates a nurturing, protective, and emotionally expansive nature. You likely find growth through caring for others and creating a sense of home.",
        "Leo": "Jupiter in Leo suggests a confident, creative, and generous approach to growth. You likely seek recognition and enjoy expressing your unique talents.",
        "Virgo": "Jupiter in Virgo points to a practical, analytical, and service-oriented approach to expansion. You likely find growth through attention to detail and helping others.",
        "Libra": "Jupiter in Libra indicates a harmonious, balanced, and relationship-focused approach to growth. You likely seek expansion through partnerships and a sense of justice.",
        "Scorpio": "Jupiter in Scorpio suggests an intense, transformative, and deeply inquisitive approach to growth. You likely find abundance through exploring the mysteries of life.",
        "Sagittarius": "Jupiter in Sagittarius points to an adventurous, philosophical, and freedom-loving approach to expansion. You likely seek growth through travel, higher learning, and new experiences.",
        "Capricorn": "Jupiter in Capricorn indicates a disciplined, ambitious, and strategic approach to growth. You likely find abundance through hard work, responsibility, and long-term planning.",
        "Aquarius": "Jupiter in Aquarius suggests an innovative, humanitarian, and unconventional approach to expansion. You likely seek growth through progressive ideas and community involvement.",
        "Pisces": "Jupiter in Pisces points to a compassionate, intuitive, and spiritually expansive nature. You likely find growth through empathy, creativity, and connection to the divine."
    },
    "Saturn": {
        "Aries": "Saturn in Aries indicates a need to learn patience, discipline, and caution in taking action. You may face challenges in asserting yourself but can develop strong leadership skills.",
        "Taurus": "Saturn in Taurus suggests a focus on building security, stability, and self-worth. You may face challenges related to finances or values but can develop resilience and determination.",
        "Gemini": "Saturn in Gemini points to a need for structure and discipline in communication and learning. You may face challenges in expressing yourself but can develop clarity and precision.",
        "Cancer": "Saturn in Cancer indicates a focus on emotional security, family, and nurturing. You may face challenges related to vulnerability but can develop emotional strength and maturity.",
        "Leo": "Saturn in Leo suggests a need to balance self-expression with responsibility. You may face challenges in seeking recognition but can develop authentic leadership and creativity.",
        "Virgo": "Saturn in Virgo points to a focus on perfection, service, and health. You may face challenges related to criticism or overwork but can develop efficiency and attention to detail.",
        "Libra": "Saturn in Libra indicates a focus on relationships, balance, and justice. You may face challenges in partnerships but can develop fairness, diplomacy, and commitment.",
        "Scorpio": "Saturn in Scorpio suggests a need for transformation, depth, and control. You may face challenges related to power or intimacy but can develop resilience and emotional strength.",
        "Sagittarius": "Saturn in Sagittarius points to a focus on beliefs, philosophies, and expansion. You may face challenges in your quest for truth but can develop wisdom and a grounded perspective.",
        "Capricorn": "Saturn in Capricorn indicates a strong sense of responsibility, ambition, and discipline. You may face challenges related to authority or achievement but can develop mastery and success.",
        "Aquarius": "Saturn in Aquarius suggests a focus on innovation, community, and individuality. You may face challenges in balancing freedom with responsibility but can develop progressive leadership.",
        "Pisces": "Saturn in Pisces points to a need for structure in spirituality, creativity, and compassion. You may face challenges related to boundaries or escapism but can develop empathy and wisdom."
    },
    "Uranus": {
        "Aries": "Uranus in Aries indicates a pioneering, innovative, and rebellious spirit. You likely seek freedom and change through bold and assertive actions.",
        "Taurus": "Uranus in Taurus suggests a focus on revolutionizing values, resources, and stability. You likely seek change through unconventional approaches to security and beauty.",
        "Gemini": "Uranus in Gemini points to a brilliant, inventive, and communicative mind. You likely seek freedom through intellectual exploration and new ideas.",
        "Cancer": "Uranus in Cancer indicates a focus on revolutionizing home, family, and emotional security. You likely seek change through unconventional approaches to nurturing and protection.",
        "Leo": "Uranus in Leo suggests a creative, dramatic, and individualistic approach to self-expression. You likely seek freedom through bold and original acts of creativity.",
        "Virgo": "Uranus in Virgo points to a focus on innovation in work, health, and service. You likely seek change through unconventional approaches to efficiency and healing.",
        "Libra": "Uranus in Libra indicates a focus on revolutionizing relationships, balance, and justice. You likely seek freedom through unconventional partnerships and a sense of fairness.",
        "Scorpio": "Uranus in Scorpio suggests an intense, transformative, and deeply inquisitive nature. You likely seek change through exploring the mysteries of life and death.",
        "Sagittarius": "Uranus in Sagittarius points to a focus on revolutionizing beliefs, philosophies, and expansion. You likely seek freedom through unconventional approaches to truth and adventure.",
        "Capricorn": "Uranus in Capricorn indicates a focus on innovation in structure, authority, and tradition. You likely seek change through unconventional approaches to responsibility and achievement.",
        "Aquarius": "Uranus in Aquarius suggests a strong sense of individuality, innovation, and humanitarianism. You likely seek freedom through progressive ideas and community involvement.",
        "Pisces": "Uranus in Pisces points to a focus on revolutionizing spirituality, creativity, and compassion. You likely seek change through unconventional approaches to empathy and the divine."
    },
    "Neptune": {
        "Aries": "Neptune in Aries indicates a dreamy, idealistic, and pioneering spirit. You likely seek transcendence through bold and assertive actions.",
        "Taurus": "Neptune in Taurus suggests a focus on spiritualizing values, resources, and stability. You likely seek transcendence through beauty, art, and the material world.",
        "Gemini": "Neptune in Gemini points to a dreamy, imaginative, and communicative mind. You likely seek transcendence through intellectual exploration and new ideas.",
        "Cancer": "Neptune in Cancer indicates a focus on spiritualizing home, family, and emotional security. You likely seek transcendence through nurturing and protection.",
        "Leo": "Neptune in Leo suggests a creative, dramatic, and idealistic approach to self-expression. You likely seek transcendence through bold and original acts of creativity.",
        "Virgo": "Neptune in Virgo points to a focus on spiritualizing work, health, and service. You likely seek transcendence through healing and attention to detail.",
        "Libra": "Neptune in Libra indicates a focus on spiritualizing relationships, balance, and justice. You likely seek transcendence through harmony and partnership.",
        "Scorpio": "Neptune in Scorpio suggests an intense, transformative, and deeply spiritual nature. You likely seek transcendence through exploring Beech mysteries of life and death.",
        "Sagittarius": "Neptune in Sagittarius points to a focus on spiritualizing beliefs, philosophies, and expansion. You likely seek transcendence through adventure and higher learning.",
        "Capricorn": "Neptune in Capricorn indicates a focus on spiritualizing structure, authority, and tradition. You likely seek transcendence through responsibility and achievement.",
        "Aquarius": "Neptune in Aquarius suggests a strong sense of individuality, innovation, and humanitarianism. You likely seek transcendence through progressive ideas and community involvement.",
        "Pisces": "Neptune in Pisces points to a deeply compassionate, intuitive, and spiritually expansive nature. You likely seek transcendence through empathy, creativity, and connection to the divine."
    },
    "Pluto": {
        "Aries": "Pluto in Aries indicates a transformative, pioneering, and assertive approach to power and change. You likely seek to revolutionize through bold and courageous actions.",
        "Taurus": "Pluto in Taurus suggests a focus on transforming values, resources, and stability. You likely seek to revolutionize through persistence and appreciation of beauty.",
        "Gemini": "Pluto in Gemini points to a transformative, communicative, and versatile approach to power and change. You likely seek to revolutionize through intellectual exploration and new ideas.",
        "Cancer": "Pluto in Cancer indicates a focus on transforming home, family, and emotional security. You likely seek to revolutionize through nurturing and protection.",
        "Leo": "Pluto in Leo suggests a creative, dramatic, and individualistic approach to power and change. You likely seek to revolutionize through bold and original acts of creativity.",
        "Virgo": "Pluto in Virgo points to a focus on transforming work, health, and service. You likely seek to revolutionize through attention to detail and healing.",
        "Libra": "Pluto in Libra indicates a focus on transforming relationships, balance, and justice. You likely seek to revolutionize through harmony and partnership.",
        "Scorpio": "Pluto in Scorpio suggests an intense, transformative, and deeply inquisitive nature. You likely seek to revolutionize through exploring the mysteries of life and death.",
        "Sagittarius": "Pluto in Sagittarius points to a focus on transforming beliefs, philosophies, and expansion. You likely seek to revolutionize through adventure and higher learning.",
        "Capricorn": "Pluto in Capricorn indicates a focus on transforming structure, authority, and tradition. You likely seek to revolutionize through responsibility and achievement.",
        "Aquarius": "Pluto in Aquarius suggests a strong sense of individuality, innovation, and humanitarianism. You likely seek to revolutionize through progressive ideas and community involvement.",
        "Pisces": "Pluto in Pisces points to a focus on transforming spirituality, creativity, and compassion. You likely seek to revolutionize through empathy and connection to the divine."
    }
}

PLANET_IN_HOUSE_INTERPRETATIONS = {
    "Sun": {
        1: "Sun in the 1st House places a strong emphasis on self-identity, personal expression, and outward appearance. You are here to shine and assert yourself.",
        2: "Sun in the 2nd House places a strong emphasis on personal values, resources, and self-worth. You are here to develop your talents and build a sense of security.",
        3: "Sun in the 3rd House highlights communication, learning, and short trips. You are likely curious and enjoy sharing your ideas with others.",
        4: "Sun in the 4th House suggests a focus on home, family, and emotional foundations. You are likely nurturing and value your roots.",
        5: "Sun in the 5th House indicates a strong need for creative expression, romance, and fun. You are likely playful and enjoy being in the spotlight.",
        6: "Sun in the 6th House points to a focus on work, health, and daily routines. You are likely diligent and strive for efficiency.",
        7: "Sun in the 7th House highlights partnerships, both personal and professional. You are likely relationship-oriented and seek balance through others.",
        8: "Sun in the 8th House suggests a focus on transformation, shared resources, and the mysteries of life. You are likely intense and drawn to deep experiences.",
        9: "Sun in the 9th House indicates a love for adventure, higher learning, and philosophical pursuits. You are likely optimistic and enjoy exploring new horizons.",
        10: "Sun in the 10th House highlights career, public image, and ambitions. You seek recognition and aim to make a mark in your chosen field.",
        11: "Sun in the 11th House highlights friendships, groups, and long-term goals. You are likely sociable and value your community.",
        12: "Sun in the 12th House suggests a focus on the subconscious, spirituality, and hidden matters. You are likely introspective and may work behind the scenes."
    },
    "Moon": {
        1: "Moon in the 1st House suggests that your emotions are readily apparent to others and play a key role in your self-expression.",
        2: "Moon in the 2nd House indicates that your emotional security is tied to your personal values and material possessions. You may have fluctuating finances but are resourceful.",
        3: "Moon in the 3rd House suggests that your emotions are closely linked to communication and learning. You likely have a strong intuition and enjoy expressing your feelings.",
        4: "Moon in the 4th House points to a deep emotional connection to home and family. You are likely nurturing and value your roots.",
        5: "Moon in the 5th House indicates that your emotions are expressed through creativity, romance, and children. You likely have a playful and affectionate nature.",
        6: "Moon in the 6th House suggests that your emotional well-being is tied to your work and health. You are likely caring and may find fulfillment in service.",
        7: "Moon in the 7th House highlights the importance of relationships in your emotional life. You are likely empathetic and seek emotional security through partnerships.",
        8: "Moon in the 8th House indicates deep emotional intensity and a fascination with the mysteries of life. You are likely intuitive and may experience emotional transformations.",
        9: "Moon in the 9th House suggests that your emotions are tied to your beliefs, philosophies, and sense of adventure. You are likely open-minded and enjoy exploring different cultures.",
        10: "Moon in the 10th House points to a strong emotional connection to your career and public image. You are likely sensitive to how others perceive you and may have a nurturing leadership style.",
        11: "Moon in the 11th House indicates that your emotions are linked to your friendships and social groups. You are likely supportive and value your community.",
        12: "Moon in the 12th House suggests a rich inner life and a need for solitude to process your emotions. You are likely empathetic and may be drawn to spiritual or healing pursuits."
    },
    "Mercury": {
        1: "Mercury in the 1st House suggests a communicative, curious, and intellectual approach to self-expression. You are likely quick-witted and enjoy sharing your thoughts.",
        2: "Mercury in the 2nd House indicates a focus on intellectual approaches to finances, values, and self-worth. You likely enjoy planning and strategizing about resources.",
        3: "Mercury in the 3rd House highlights a strong emphasis on communication, learning, and mental agility. You are likely versatile and excel in intellectual pursuits.",
        4: "Mercury in the 4th House suggests a mind focused on home, family, and emotional foundations. You likely enjoy discussing or analyzing your roots.",
        5: "Mercury in the 5th House indicates a playful, creative, and expressive communication style. You likely enjoy intellectual games, storytelling, or romance.",
        6: "Mercury in the 6th House points to an analytical mind focused on work, health, and routines. You likely excel at problem-solving and organization.",
        7: "Mercury in the 7th House highlights communication in partnerships. You are likely diplomatic and enjoy intellectual exchanges with others.",
        8: "Mercury in the 8th House suggests a deep, investigative mind drawn to mysteries and transformation. You likely enjoy research and exploring hidden truths.",
        9: "Mercury in the 9th House indicates a love for broad-minded thinking, philosophy, and travel. You are likely curious about different cultures and ideas.",
        10: "Mercury in the 10th House highlights a career focused on communication, intellect, or teaching. You likely value clarity and precision in your public life.",
        11: "Mercury in the 11th House suggests a mind focused on friendships, groups, and innovative ideas. You likely enjoy networking and intellectual discussions.",
        12: "Mercury in the 12th House indicates a reflective, intuitive mind drawn to the subconscious. You are likely imaginative and may excel in creative writing or spiritual pursuits."
    },
    "Venus": {
        1: "Venus in the 1st House suggests a charming, attractive, and harmonious approach to self-expression. You are likely sociable and value beauty.",
        2: "Venus in the 2nd House indicates a love for luxury, comfort, and material security. You likely attract wealth and enjoy sensual pleasures.",
        3: "Venus in the 3rd House highlights a pleasant, diplomatic communication style. You are likely charming in conversation and enjoy intellectual connections.",
        4: "Venus in the 4th House suggests a focus on creating a beautiful, harmonious home environment. You likely value family and comfort.",
        5: "Venus in the 5th House indicates a strong need for romance, creativity, and pleasure. You are likely affectionate and enjoy artistic pursuits.",
        6: "Venus in the 6th House points to a love for service, health, and harmony in daily routines. You likely express affection through acts of care.",
        7: "Venus in the 7th House highlights a strong focus on relationships and partnerships. You are likely romantic and seek balance with others.",
        8: "Venus in the 8th House suggests a passionate, intense approach to love and shared resources. You are likely drawn to deep, transformative connections.",
        9: "Venus in the 9th House indicates a love for adventure, culture, and philosophical pursuits in relationships. You are likely attracted to diversity and exploration.",
        10: "Venus in the 10th House highlights a career focused on beauty, art, or relationships. You likely seek public approval and harmony in your professional life.",
        11: "Venus in the 11th House suggests a love for friendships, social causes, and group harmony. You are likely popular and value community.",
        12: "Venus in the 12th House indicates a romantic, compassionate, and spiritual approach to love. You are likely drawn to secret or selfless affections."
    },
    "Mars": {
        1: "Mars in the 1st House suggests a bold, assertive, and energetic approach to self-expression. You are likely a natural leader with strong initiative.",
        2: "Mars in the 2nd House indicates a drive to acquire resources and build security. You are likely determined and protective of your possessions.",
        3: "Mars in the 3rd House highlights an assertive, quick, and dynamic communication style. You are likely passionate in debates and intellectual pursuits.",
        4: "Mars in the 4th House suggests a strong drive to protect home and family. You are likely energetic in domestic matters and may experience family conflicts.",
        5: "Mars in the 5th House indicates a passionate, competitive approach to creativity, romance, and fun. You are likely bold and enjoy taking risks.",
        6: "Mars in the 6th House points to a strong work ethic and energy directed toward health and service. You are likely efficient but may push yourself hard.",
        7: "Mars in the 7th House highlights a dynamic, assertive approach to partnerships. You are likely passionate but may encounter conflicts in relationships.",
        8: "Mars in the 8th House suggests intense energy focused on transformation, shared resources, and power. You are likely fearless and drawn to deep experiences.",
        9: "Mars in the 9th House indicates a bold, adventurous approach to learning and exploration. You are likely passionate about your beliefs and enjoy challenges.",
        10: "Mars in the 10th House highlights ambition, drive, and leadership in your career. You are likely determined to succeed and take initiative publicly.",
        11: "Mars in the 11th House suggests energy directed toward friendships, groups, and goals. You are likely a motivating force in your community.",
        12: "Mars in the 12th House indicates hidden or subconscious drives. You are likely introspective and may channel energy into spiritual or behind-the-scenes efforts."
    },
    "Jupiter": {
        1: "Jupiter in the 1st House suggests an optimistic, expansive, and generous approach to self-expression. You are likely confident and attract opportunities.",
        2: "Jupiter in the 2nd House indicates a focus on abundance, wealth, and personal values. You are likely lucky in financial matters and enjoy growth.",
        3: "Jupiter in the 3rd House highlights a broad-minded, communicative approach to learning. You are likely enthusiastic about sharing knowledge.",
        4: "Jupiter in the 4th House suggests a focus on expanding home and family life. You are likely generous and find comfort in your roots.",
        5: "Jupiter in the 5th House indicates a love for creativity, romance, and enjoyment. You are likely playful and attract good fortune in these areas.",
        6: "Jupiter in the 6th House points to growth through work, health, and service. You are likely optimistic and find fulfillment in helping others.",
        7: "Jupiter in the 7th House highlights expansion through partnerships. You are likely lucky in relationships and value harmony and growth.",
        8: "Jupiter in the 8th House suggests a focus on transformation and shared resources. You are likely insightful and attract opportunities through depth.",
        9: "Jupiter in the 9th House indicates a strong love for adventure, philosophy, and higher learning. You are likely optimistic and seek wisdom.",
        10: "Jupiter in the 10th House highlights success, recognition, and growth in your career. You are likely ambitious and attract professional opportunities.",
        11: "Jupiter in the 11th House suggests expansion through friendships and social causes. You are likely sociable and inspire others in groups.",
        12: "Jupiter in the 12th House indicates a spiritual, compassionate approach to growth. You are likely intuitive and find abundance in solitude."
    },
    "Saturn": {
        1: "Saturn in the 1st House suggests a serious, disciplined approach to self-expression. You may face challenges but develop strength and maturity.",
        2: "Saturn in the 2nd House indicates a focus on building security and self-worth through effort. You may face financial delays but gain resilience.",
        3: "Saturn in the 3rd House highlights a need for structure in communication and learning. You may face mental challenges but develop clarity.",
        4: "Saturn in the 4th House suggests a focus on responsibility in home and family life. You may face emotional restrictions but build a solid foundation.",
        5: "Saturn in the 5th House indicates a disciplined approach to creativity and romance. You may face delays but develop authentic expression.",
        6: "Saturn in the 6th House points to a strong sense of duty in work and health. You may face challenges but excel through persistence.",
        7: "Saturn in the 7th House highlights responsibility in partnerships. You may face relationship tests but develop commitment and balance.",
        8: "Saturn in the 8th House suggests a focus on discipline in transformation and shared resources. You may face power struggles but gain depth.",
        9: "Saturn in the 9th House indicates a serious approach to beliefs and learning. You may face philosophical challenges but develop wisdom.",
        10: "Saturn in the 10th House highlights ambition and responsibility in your career. You may face obstacles but achieve lasting success.",
        11: "Saturn in the 11th House suggests a focus on structure in friendships and goals. You may face social limitations but build strong alliances.",
        12: "Saturn in the 12th House indicates a need for discipline in spiritual and subconscious matters. You may face isolation but gain inner strength."
    },
    "Uranus": {
        1: "Uranus in the 1st House suggests an innovative, independent approach to self-expression. You are likely unique and value freedom.",
        2: "Uranus in the 2nd House indicates sudden changes in finances and values. You are likely unconventional in how you handle resources.",
        3: "Uranus in the 3rd House highlights a brilliant, inventive mind. You are likely original in your thoughts and communication.",
        4: "Uranus in the 4th House suggests an unconventional approach to home and family. You are likely restless and seek change in your roots.",
        5: "Uranus in the 5th House indicates a creative, unpredictable approach to romance and self-expression. You are likely spontaneous and innovative.",
        6: "Uranus in the 6th House points to an unconventional approach to work and health. You are likely inventive and seek freedom in routines.",
        7: "Uranus in the 7th House highlights a need for independence in partnerships. You are likely attracted to unique relationships.",
        8: "Uranus in the 8th House suggests sudden transformations and insights into mysteries. You are likely drawn to change and the unconventional.",
        9: "Uranus in the 9th House indicates a revolutionary approach to beliefs and learning. You are likely progressive and enjoy exploring new ideas.",
        10: "Uranus in the 10th House highlights an innovative, unconventional career path. You are likely a trailblazer in your public life.",
        11: "Uranus in the 11th House suggests a focus on freedom in friendships and groups. You are likely visionary and attract like-minded individuals.",
        12: "Uranus in the 12th House indicates a subconscious drive for change and innovation. You are likely intuitive and drawn to the unusual."
    },
    "Neptune": {
        1: "Neptune in the 1st House suggests a dreamy, sensitive approach to self-expression. You are likely compassionate and may seem mysterious.",
        2: "Neptune in the 2nd House indicates a spiritual or idealistic approach to finances and values. You may face confusion but seek transcendence.",
        3: "Neptune in the 3rd House highlights an imaginative, intuitive mind. You are likely poetic and may struggle with clarity.",
        4: "Neptune in the 4th House suggests a dreamy, emotional connection to home and family. You are likely nurturing but may idealize your roots.",
        5: "Neptune in the 5th House indicates a romantic, creative approach to self-expression. You are likely artistic and seek inspiration.",
        6: "Neptune in the 6th House points to a compassionate approach to work and health. You are likely intuitive but may need boundaries.",
        7: "Neptune in the 7th House highlights a spiritual, idealistic view of partnerships. You are likely romantic but may face disillusionment.",
        8: "Neptune in the 8th House suggests a deep, mystical approach to transformation. You are likely intuitive and drawn to the unseen.",
        9: "Neptune in the 9th House indicates a spiritual, philosophical approach to learning. You are likely inspired by higher ideals and travel.",
        10: "Neptune in the 10th House highlights a career tied to creativity or compassion. You are likely visionary but may lack practicality.",
        11: "Neptune in the 11th House suggests a focus on idealistic friendships and causes. You are likely empathetic and drawn to humanitarian goals.",
        12: "Neptune in the 12th House indicates a strong connection to the subconscious and spirituality. You are likely intuitive and seek transcendence."
    },
    "Pluto": {
        1: "Pluto in the 1st House suggests a powerful, transformative approach to self-expression. You are likely intense and magnetic.",
        2: "Pluto in the 2nd House indicates a focus on transforming finances and values. You are likely resourceful and face deep changes.",
        3: "Pluto in the 3rd House highlights a penetrating, investigative mind. You are likely intense in communication and seek truth.",
        4: "Pluto in the 4th House suggests a transformative approach to home and family. You are likely deep and may face emotional upheaval.",
        5: "Pluto in the 5th House indicates a powerful, intense approach to creativity and romance. You are likely passionate and transformative.",
        6: "Pluto in the 6th House points to a focus on transformation in work and health. You are likely driven and seek profound change.",
        7: "Pluto in the 7th House highlights intensity in partnerships. You are likely drawn to powerful relationships and transformation.",
        8: "Pluto in the 8th House suggests a natural focus on power, transformation, and shared resources. You are likely deep and resilient.",
        9: "Pluto in the 9th House indicates a transformative approach to beliefs and learning. You are likely intense and seek profound wisdom.",
        10: "Pluto in the 10th House highlights a powerful, transformative career path. You are likely ambitious and drawn to influence.",
        11: "Pluto in the 11th House suggests a focus on transformation in friendships and goals. You are likely intense and visionary.",
        12: "Pluto in the 12th House indicates a deep, subconscious drive for change. You are likely introspective and drawn to the hidden."
    }
}

"""Expanded Aspect Interpretations with All Planet Pairs and Special Points for Major Aspects"""

ASPECT_INTERPRETATIONS = {
    "Conjunction": {
        # Existing planet-planet conjunctions
        ("Sun", "Moon"): "Sun conjunct Moon indicates a blending of your conscious will and emotional nature, creating a strong sense of self and purpose.",
        ("Sun", "Mercury"): "Sun conjunct Mercury indicates a close alignment between your identity and your communication style. You are likely articulate and enjoy expressing your thoughts.",
        ("Sun", "Venus"): "Sun conjunct Venus suggests a harmonious blend of your identity and values, making you charming, sociable, and appreciative of beauty.",
        ("Sun", "Mars"): "Sun conjunct Mars indicates a fusion of your will and drive, giving you strong energy, courage, and a competitive spirit.",
        ("Sun", "Jupiter"): "Sun conjunct Jupiter suggests an expansive, optimistic nature, blending your identity with growth, luck, and a philosophical outlook.",
        ("Sun", "Saturn"): "Sun conjunct Saturn indicates a serious, disciplined approach to life, blending your identity with responsibility and structure.",
        ("Sun", "Uranus"): "Sun conjunct Uranus suggests an innovative, rebellious spirit, blending your identity with originality and a desire for freedom.",
        ("Sun", "Neptune"): "Sun conjunct Neptune indicates a dreamy, spiritual nature, blending your identity with intuition, creativity, and idealism.",
        ("Sun", "Pluto"): "Sun conjunct Pluto suggests a powerful, transformative energy, blending your identity with intensity, depth, and a drive for control.",
        ("Moon", "Mercury"): "Moon conjunct Mercury indicates a fusion of emotions and intellect, making you intuitive, communicative, and sensitive in your thinking.",
        ("Moon", "Venus"): "Moon conjunct Venus indicates a fusion of emotions and affection, making you deeply loving and sensitive to beauty.",
        ("Moon", "Mars"): "Moon conjunct Mars suggests a blending of emotions and drive, giving you passionate, impulsive, and sometimes volatile reactions.",
        ("Moon", "Jupiter"): "Moon conjunct Jupiter indicates an optimistic, generous emotional nature, blending feelings with growth and expansiveness.",
        ("Moon", "Saturn"): "Moon conjunct Saturn suggests a serious, reserved emotional nature, blending feelings with discipline and responsibility.",
        ("Moon", "Uranus"): "Moon conjunct Uranus indicates an unpredictable, independent emotional nature, blending feelings with originality and sudden changes.",
        ("Moon", "Neptune"): "Moon conjunct Neptune suggests a highly intuitive, empathetic emotional nature, blending feelings with spirituality and imagination.",
        ("Moon", "Pluto"): "Moon conjunct Pluto indicates intense, transformative emotions, blending feelings with depth, power, and sometimes obsession.",
        ("Mercury", "Venus"): "Mercury conjunct Venus suggests a harmonious blend of intellect and aesthetics, making you charming, diplomatic, and creative in communication.",
        ("Mercury", "Mars"): "Mercury conjunct Mars indicates a sharp, assertive mind, blending intellect with drive, making you quick-witted and sometimes argumentative.",
        ("Mercury", "Jupiter"): "Mercury conjunct Jupiter suggests an expansive, philosophical mind, blending intellect with optimism and a love for learning.",
        ("Mercury", "Saturn"): "Mercury conjunct Saturn indicates a disciplined, serious mind, blending intellect with structure and a focus on practical matters.",
        ("Mercury", "Uranus"): "Mercury conjunct Uranus suggests an innovative, original mind, blending intellect with sudden insights and unconventional thinking.",
        ("Mercury", "Neptune"): "Mercury conjunct Neptune indicates an imaginative, intuitive mind, blending intellect with creativity and sometimes confusion.",
        ("Mercury", "Pluto"): "Mercury conjunct Pluto suggests a deep, investigative mind, blending intellect with intensity and a desire to uncover hidden truths.",
        ("Venus", "Mars"): "Venus conjunct Mars suggests a blending of your desires for love and action. You are likely passionate and may have a strong creative drive.",
        ("Venus", "Jupiter"): "Venus conjunct Jupiter indicates a generous, optimistic approach to love and beauty, blending affection with growth and expansiveness.",
        ("Venus", "Saturn"): "Venus conjunct Saturn suggests a serious, committed approach to love and values, blending affection with responsibility and sometimes restriction.",
        ("Venus", "Uranus"): "Venus conjunct Uranus indicates an unconventional, exciting approach to love and beauty, blending affection with originality and sudden changes.",
        ("Venus", "Neptune"): "Venus conjunct Neptune suggests a romantic, idealistic approach to love, blending affection with spirituality and imagination.",
        ("Venus", "Pluto"): "Venus conjunct Pluto indicates an intense, transformative approach to love, blending affection with depth, power, and sometimes obsession.",
        ("Mars", "Jupiter"): "Mars conjunct Jupiter suggests abundant energy and enthusiasm for action, leading to bold and optimistic pursuits.",
        ("Mars", "Saturn"): "Mars conjunct Saturn indicates a disciplined, controlled approach to action, blending drive with structure and sometimes frustration.",
        ("Mars", "Uranus"): "Mars conjunct Uranus suggests an impulsive, innovative approach to action, blending drive with originality and sudden changes.",
        ("Mars", "Neptune"): "Mars conjunct Neptune indicates a spiritual, imaginative approach to action, blending drive with intuition and sometimes confusion.",
        ("Mars", "Pluto"): "Mars conjunct Pluto suggests a powerful, intense approach to action, blending drive with transformation and a desire for control.",
        ("Jupiter", "Saturn"): "Jupiter conjunct Saturn indicates a balance between expansion and contraction, blending optimism with discipline and realism.",
        ("Jupiter", "Uranus"): "Jupiter conjunct Uranus suggests an expansive, innovative approach to growth, blending optimism with originality and sudden opportunities.",
        ("Jupiter", "Neptune"): "Jupiter conjunct Neptune indicates a spiritual, idealistic approach to growth, blending optimism with imagination and compassion.",
        ("Jupiter", "Pluto"): "Jupiter conjunct Pluto suggests a powerful, transformative approach to growth, blending optimism with intensity and a drive for power.",
        ("Saturn", "Uranus"): "Saturn conjunct Uranus indicates a tension between tradition and innovation, blending structure with originality and change.",
        ("Saturn", "Neptune"): "Saturn conjunct Neptune suggests a blend of realism and idealism, blending structure with imagination and sometimes confusion.",
        ("Saturn", "Pluto"): "Saturn conjunct Pluto indicates a powerful, transformative approach to structure, blending discipline with intensity and control.",
        ("Uranus", "Neptune"): "Uranus conjunct Neptune suggests a fusion of innovation and spirituality, blending originality with intuition and idealism.",
        ("Uranus", "Pluto"): "Uranus conjunct Pluto indicates a powerful drive for change and transformation, blending originality with intensity and revolution.",
        ("Neptune", "Pluto"): "Neptune conjunct Pluto suggests a deep, transformative spirituality, blending imagination with intensity and a desire for transcendence.",

        # New entries for MeanNode
        ("Sun", "MeanNode"): "Sun conjunct MeanNode suggests that your sense of self and purpose is closely aligned with your karmic path. You are here to express your individuality and leadership qualities in a way that supports your life direction.",
        ("Moon", "MeanNode"): "Moon conjunct MeanNode indicates that your emotional nature and nurturing abilities are closely tied to your karmic path. You are encouraged to develop your intuition and emotional intelligence.",
        ("Mercury", "MeanNode"): "Mercury conjunct MeanNode suggests that your communication style and thought processes are closely aligned with your karmic path. You are here to express your ideas and connect with others in a way that supports your life direction.",
        ("Venus", "MeanNode"): "Venus conjunct MeanNode indicates that your values, relationships, and creative talents are closely tied to your karmic path. You are encouraged to develop your sense of beauty and harmony.",
        ("Mars", "MeanNode"): "Mars conjunct MeanNode suggests that your drive, assertiveness, and courage are closely aligned with your karmic path. You are here to take action and pursue your goals in a way that supports your life direction.",
        ("Jupiter", "MeanNode"): "Jupiter conjunct MeanNode indicates that your optimism, generosity, and philosophical outlook are closely tied to your karmic path. You are encouraged to expand your horizons and seek wisdom.",
        ("Saturn", "MeanNode"): "Saturn conjunct MeanNode suggests that your discipline, responsibility, and structure are closely aligned with your karmic path. You are here to build a solid foundation and achieve your goals through hard work.",
        ("Uranus", "MeanNode"): "Uranus conjunct MeanNode indicates that your originality, innovation, and desire for freedom are closely tied to your karmic path. You are encouraged to embrace change and express your unique perspective.",
        ("Neptune", "MeanNode"): "Neptune conjunct MeanNode suggests that your intuition, spirituality, and imagination are closely aligned with your karmic path. You are here to develop your compassion and connect with the divine.",
        ("Pluto", "MeanNode"): "Pluto conjunct MeanNode indicates that your intensity, depth, and transformative power are closely tied to your karmic path. You are encouraged to embrace change and explore the mysteries of life.",

        # New entries for Ascendant
        ("Sun", "Ascendant"): "Sun conjunct Ascendant suggests that you have a strong, confident personality and are likely to be seen as a leader or authority figure. Your sense of self is closely tied to how you present yourself to the world.",
        ("Moon", "Ascendant"): "Moon conjunct Ascendant indicates that your emotional nature and nurturing abilities are readily apparent to others. You may be seen as approachable, caring, and intuitive.",
        ("Mercury", "Ascendant"): "Mercury conjunct Ascendant suggests that your communication style and thought processes are integral to your personality. You may be seen as articulate, curious, and quick-witted.",
        ("Venus", "Ascendant"): "Venus conjunct Ascendant indicates that your values, relationships, and creative talents are expressed through your personality. You may be seen as charming, attractive, and diplomatic.",
        ("Mars", "Ascendant"): "Mars conjunct Ascendant suggests that your drive, assertiveness, and courage are integral to your personality. You may be seen as energetic, competitive, and action-oriented.",
        ("Jupiter", "Ascendant"): "Jupiter conjunct Ascendant indicates that your optimism, generosity, and philosophical outlook are expressed through your personality. You may be seen as enthusiastic, adventurous, and wise.",
        ("Saturn", "Ascendant"): "Saturn conjunct Ascendant suggests that your discipline, responsibility, and structure are integral to your personality. You may be seen as serious, reliable, and hardworking.",
        ("Uranus", "Ascendant"): "Uranus conjunct Ascendant indicates that your originality, innovation, and desire for freedom are expressed through your personality. You may be seen as unique, unconventional, and independent.",
        ("Neptune", "Ascendant"): "Neptune conjunct Ascendant suggests that your intuition, spirituality, and imagination are integral to your personality. You may be seen as dreamy, compassionate, and artistic.",
        ("Pluto", "Ascendant"): "Pluto conjunct Ascendant indicates that your intensity, depth, and transformative power are expressed through your personality. You may be seen as magnetic, powerful, and mysterious.",

        # New entries for MidHeaven
        ("Sun", "MidHeaven"): "Sun conjunct MidHeaven suggests that your sense of self and purpose is closely tied to your career and public image. You are likely to achieve recognition and success in your professional life.",
        ("Moon", "MidHeaven"): "Moon conjunct MidHeaven indicates that your emotional nature and nurturing abilities are integral to your career and public image. You may be seen as caring, intuitive, and supportive in your professional life.",
        ("Mercury", "MidHeaven"): "Mercury conjunct MidHeaven suggests that your communication style and thought processes are closely tied to your career and public image. You may be seen as articulate, knowledgeable, and quick-witted in your professional life.",
        ("Venus", "MidHeaven"): "Venus conjunct MidHeaven indicates that your values, relationships, and creative talents are integral to your career and public image. You may be seen as charming, diplomatic, and artistic in your professional life.",
        ("Mars", "MidHeaven"): "Mars conjunct MidHeaven suggests that your drive, assertiveness, and courage are closely tied to your career and public image. You may be seen as energetic, competitive, and action-oriented in your professional life.",
        ("Jupiter", "MidHeaven"): "Jupiter conjunct MidHeaven indicates that your optimism, generosity, and philosophical outlook are integral to your career and public image. You may be seen as enthusiastic, adventurous, and wise in your professional life.",
        ("Saturn", "MidHeaven"): "Saturn conjunct MidHeaven suggests that your discipline, responsibility, and structure are closely tied to your career and public image. You may be seen as serious, reliable, and hardworking in your professional life.",
        ("Uranus", "MidHeaven"): "Uranus conjunct MidHeaven indicates that your originality, innovation, and desire for freedom are integral to your career and public image. You may be seen as unique, unconventional, and independent in your professional life.",
        ("Neptune", "MidHeaven"): "Neptune conjunct MidHeaven suggests that your intuition, spirituality, and imagination are closely tied to your career and public image. You may be seen as dreamy, compassionate, and artistic in your professional life.",
        ("Pluto", "MidHeaven"): "Pluto conjunct MidHeaven indicates that your intensity, depth, and transformative power are integral to your career and public image. You may be seen as magnetic, powerful, and mysterious in your professional life."
    },
    "Sextile": {
        # Existing planet-planet sextiles
        ("Sun", "Moon"): "Sun sextile Moon suggests an easy flow between your conscious will and emotions, enhancing self-awareness and balance.",
        ("Sun", "Mercury"): "Sun sextile Mercury indicates a harmonious blend of identity and intellect, making you clear and confident in communication.",
        ("Sun", "Venus"): "Sun sextile Venus suggests a pleasant alignment of identity and values, enhancing your charm and social ease.",
        ("Sun", "Mars"): "Sun sextile Mars indicates a harmonious flow of energy between your identity and your drive, making you confident and effective.",
        ("Sun", "Jupiter"): "Sun sextile Jupiter suggests an easy flow between your identity and growth, bringing optimism, luck, and a sense of purpose.",
        ("Sun", "Saturn"): "Sun sextile Saturn indicates a harmonious relationship between your identity and discipline, making you responsible and capable of achieving goals.",
        ("Sun", "Uranus"): "Sun sextile Uranus suggests a harmonious blend of your identity and originality, making you innovative and open to change.",
        ("Sun", "Neptune"): "Sun sextile Neptune indicates an easy flow between your identity and spirituality, enhancing your intuition and creativity.",
        ("Sun", "Pluto"): "Sun sextile Pluto suggests a harmonious relationship between your identity and transformation, making you powerful and capable of deep change.",
        ("Moon", "Mercury"): "Moon sextile Mercury indicates a harmonious blend of emotions and intellect, making you intuitive and communicative.",
        ("Moon", "Venus"): "Moon sextile Venus indicates a harmonious relationship between your emotions and your values. You likely have a gentle and affectionate nature.",
        ("Moon", "Mars"): "Moon sextile Mars suggests an easy flow between emotions and drive, making you passionate and effective in action.",
        ("Moon", "Jupiter"): "Moon sextile Jupiter indicates a harmonious relationship between emotions and growth, bringing optimism and emotional generosity.",
        ("Moon", "Saturn"): "Moon sextile Saturn suggests a balance between emotions and discipline, making you emotionally mature and responsible.",
        ("Moon", "Uranus"): "Moon sextile Uranus indicates an easy flow between emotions and originality, making you open to change and emotionally independent.",
        ("Moon", "Neptune"): "Moon sextile Neptune suggests a harmonious blend of emotions and intuition, enhancing your empathy and imagination.",
        ("Moon", "Pluto"): "Moon sextile Pluto indicates a harmonious relationship between emotions and transformation, making you emotionally resilient and deep.",
        ("Mercury", "Venus"): "Mercury sextile Venus suggests a pleasant, diplomatic way of communicating, enhancing your social charm and creativity.",
        ("Mercury", "Mars"): "Mercury sextile Mars suggests a harmonious blend of intellect and drive, making you quick-witted and effective in communication.",
        ("Mercury", "Jupiter"): "Mercury sextile Jupiter indicates an easy flow between intellect and growth, enhancing your learning and philosophical thinking.",
        ("Mercury", "Saturn"): "Mercury sextile Saturn suggests a balance between intellect and discipline, making you practical and focused in your thinking.",
        ("Mercury", "Uranus"): "Mercury sextile Uranus indicates a harmonious relationship between intellect and originality, making you innovative and insightful.",
        ("Mercury", "Neptune"): "Mercury sextile Neptune suggests an easy flow between intellect and intuition, enhancing your creativity and imagination.",
        ("Mercury", "Pluto"): "Mercury sextile Pluto indicates a harmonious blend of intellect and depth, making you investigative and perceptive.",
        ("Venus", "Mars"): "Venus sextile Mars suggests a harmonious relationship between love and action, making you passionate and attractive.",
        ("Venus", "Jupiter"): "Venus sextile Jupiter indicates an easy flow between love and growth, bringing luck and generosity in relationships.",
        ("Venus", "Saturn"): "Venus sextile Saturn suggests a balance between love and discipline, making you committed and responsible in relationships.",
        ("Venus", "Uranus"): "Venus sextile Uranus indicates a harmonious blend of love and originality, making you open to unconventional relationships.",
        ("Venus", "Neptune"): "Venus sextile Neptune suggests an easy flow between love and spirituality, enhancing your romantic and artistic nature.",
        ("Venus", "Pluto"): "Venus sextile Pluto indicates a harmonious relationship between love and transformation, making you intense and magnetic in relationships.",
        ("Mars", "Jupiter"): "Mars sextile Jupiter suggests a harmonious blend of drive and growth, making you enthusiastic and effective in pursuing goals.",
        ("Mars", "Saturn"): "Mars sextile Saturn indicates a balance between drive and discipline, making you persistent and capable of achieving long-term success.",
        ("Mars", "Uranus"): "Mars sextile Uranus suggests an easy flow between drive and originality, making you innovative and effective in action.",
        ("Mars", "Neptune"): "Mars sextile Neptune indicates a harmonious relationship between drive and intuition, enhancing your spiritual and creative pursuits.",
        ("Mars", "Pluto"): "Mars sextile Pluto suggests a harmonious blend of drive and transformation, making you powerful and capable of profound change.",
        ("Jupiter", "Saturn"): "Jupiter sextile Saturn suggests a balance between expansion and discipline. You are likely able to manifest your goals through careful planning and optimism.",
        ("Jupiter", "Uranus"): "Jupiter sextile Uranus indicates an easy flow between growth and originality, bringing opportunities for innovation and expansion.",
        ("Jupiter", "Neptune"): "Jupiter sextile Neptune suggests a harmonious relationship between growth and spirituality, enhancing your faith and compassion.",
        ("Jupiter", "Pluto"): "Jupiter sextile Pluto indicates a harmonious blend of growth and transformation, making you capable of profound and expansive change.",
        ("Saturn", "Uranus"): "Saturn sextile Uranus suggests a balance between structure and innovation, making you capable of implementing progressive changes.",
        ("Saturn", "Neptune"): "Saturn sextile Neptune indicates a harmonious relationship between discipline and intuition, enhancing your ability to manifest dreams.",
        ("Saturn", "Pluto"): "Saturn sextile Pluto suggests a harmonious blend of discipline and transformation, making you capable of profound and lasting change.",
        ("Uranus", "Neptune"): "Uranus sextile Neptune indicates a creative blend of innovation and intuition, leading to inspired and visionary ideas.",
        ("Uranus", "Pluto"): "Uranus sextile Pluto indicates an easy flow between originality and transformation, making you a catalyst for revolutionary change.",
        ("Neptune", "Pluto"): "Neptune sextile Pluto suggests a harmonious relationship between intuition and depth, enhancing your spiritual and transformative power.",

        # New entries for MeanNode
        ("Sun", "MeanNode"): "Sun sextile MeanNode suggests that your sense of self and purpose can support your karmic growth. You may find opportunities to express your individuality and leadership qualities in a way that aligns with your life direction.",
        ("Moon", "MeanNode"): "Moon sextile MeanNode indicates that your emotional nature and nurturing abilities can support your karmic growth. You may find opportunities to develop your intuition and emotional intelligence.",
        ("Mercury", "MeanNode"): "Mercury sextile MeanNode suggests that your communication style and thought processes can support your karmic growth. You may find opportunities to express your ideas and connect with others in a way that aligns with your life direction.",
        ("Venus", "MeanNode"): "Venus sextile MeanNode indicates that your values, relationships, and creative talents can support your karmic growth. You may find opportunities to develop your sense of beauty and harmony.",
        ("Mars", "MeanNode"): "Mars sextile MeanNode suggests that your drive, assertiveness, and courage can support your karmic growth. You may find opportunities to take action and pursue your goals in a way that aligns with your life direction.",
        ("Jupiter", "MeanNode"): "Jupiter sextile MeanNode indicates that your optimism, generosity, and philosophical outlook can support your karmic growth. You may find opportunities to expand your horizons and seek wisdom.",
        ("Saturn", "MeanNode"): "Saturn sextile MeanNode suggests that your discipline, responsibility, and structure can support your karmic growth. You may find opportunities to build a solid foundation and achieve your goals through hard work.",
        ("Uranus", "MeanNode"): "Uranus sextile MeanNode indicates that your originality, innovation, and desire for freedom can support your karmic growth. You may find opportunities to embrace change and express your unique perspective.",
        ("Neptune", "MeanNode"): "Neptune sextile MeanNode suggests that your intuition, spirituality, and imagination can support your karmic growth. You may find opportunities to develop your compassion and connect with the divine.",
        ("Pluto", "MeanNode"): "Pluto sextile MeanNode indicates that your intensity, depth, and transformative power can support your karmic growth. You may find opportunities to embrace change and explore the mysteries of life.",

        # New entries for Ascendant
        ("Sun", "Ascendant"): "Sun sextile Ascendant suggests that your sense of self and purpose can support your self-expression and interactions with others. You may find opportunities to express your individuality and leadership qualities in a way that aligns with your personality.",
        ("Moon", "Ascendant"): "Moon sextile Ascendant indicates that your emotional nature and nurturing abilities can support your self-expression and interactions with others. You may find opportunities to connect with others through your empathy and intuition.",
        ("Mercury", "Ascendant"): "Mercury sextile Ascendant suggests that your communication style and thought processes can support your self-expression and interactions with others. You may find opportunities to express your ideas and connect with others in a way that aligns with your personality.",
        ("Venus", "Ascendant"): "Venus sextile Ascendant indicates that your values, relationships, and creative talents can support your self-expression and interactions with others. You may find opportunities to develop your sense of beauty and harmony.",
        ("Mars", "Ascendant"): "Mars sextile Ascendant suggests that your drive, assertiveness, and courage can support your self-expression and interactions with others. You may find opportunities to take action and pursue your goals in a way that aligns with your personality.",
        ("Jupiter", "Ascendant"): "Jupiter sextile Ascendant indicates that your optimism, generosity, and philosophical outlook can support your self-expression and interactions with others. You may find opportunities to expand your horizons and seek wisdom.",
        ("Saturn", "Ascendant"): "Saturn sextile Ascendant suggests that your discipline, responsibility, and structure can support your self-expression and interactions with others. You may find opportunities to build a solid foundation and achieve your goals through hard work.",
        ("Uranus", "Ascendant"): "Uranus sextile Ascendant indicates that your originality, innovation, and desire for freedom can support your self-expression and interactions with others. You may find opportunities to embrace change and express your unique perspective.",
        ("Neptune", "Ascendant"): "Neptune sextile Ascendant suggests that your intuition, spirituality, and imagination can support your self-expression and interactions with others. You may find opportunities to develop your compassion and connect with the divine.",
        ("Pluto", "Ascendant"): "Pluto sextile Ascendant indicates that your intensity, depth, and transformative power can support your self-expression and interactions with others. You may find opportunities to embrace change and explore the mysteries of life.",

        # New entries for MidHeaven
        ("Sun", "MidHeaven"): "Sun sextile MidHeaven suggests that your sense of self and purpose can support your career and public image. You may find opportunities to express your individuality and leadership qualities in a way that aligns with your professional life.",
        ("Moon", "MidHeaven"): "Moon sextile MidHeaven indicates that your emotional nature and nurturing abilities can support your career and public image. You may find opportunities to develop your intuition and emotional intelligence in your professional life.",
        ("Mercury", "MidHeaven"): "Mercury sextile MidHeaven suggests that your communication style and thought processes can support your career and public image. You may find opportunities to express your ideas and connect with others in a way that aligns with your professional life.",
        ("Venus", "MidHeaven"): "Venus sextile MidHeaven indicates that your values, relationships, and creative talents can support your career and public image. You may find opportunities to develop your sense of beauty and harmony in your professional life.",
        ("Mars", "MidHeaven"): "Mars sextile MidHeaven suggests that your drive, assertiveness, and courage can support your career and public image. You may find opportunities to take action and pursue your goals in a way that aligns with your professional life.",
        ("Jupiter", "MidHeaven"): "Jupiter sextile MidHeaven indicates that your optimism, generosity, and philosophical outlook can support your career and public image. You may find opportunities to expand your horizons and seek wisdom in your professional life.",
        ("Saturn", "MidHeaven"): "Saturn sextile MidHeaven suggests that your discipline, responsibility, and structure can support your career and public image. You may find opportunities to build a solid foundation and achieve your goals through hard work in your professional life.",
        ("Uranus", "MidHeaven"): "Uranus sextile MidHeaven indicates that your originality, innovation, and desire for freedom can support your career and public image. You may find opportunities to embrace change and express your unique perspective in your professional life.",
        ("Neptune", "MidHeaven"): "Neptune sextile MidHeaven suggests that your intuition, spirituality, and imagination can support your career and public image. You may find opportunities to develop your compassion and connect with the divine in your professional life.",
        ("Pluto", "MidHeaven"): "Pluto sextile MidHeaven indicates that your intensity, depth, and transformative power can support your career and public image. You may find opportunities to embrace change and explore the mysteries of life in your professional life."
    },
    "Square": {
        # Existing planet-planet squares
        ("Sun", "Moon"): "Sun square Moon suggests tension between your conscious will and emotional needs, potentially leading to inner conflict or challenges in balancing goals and feelings.",
        ("Sun", "Mercury"): "Sun square Mercury indicates a conflict between your identity and communication, potentially causing misunderstandings or overthinking your self-expression.",
        ("Sun", "Venus"): "Sun square Venus suggests tension between your identity and values, potentially leading to struggles in relationships or self-worth.",
        ("Sun", "Mars"): "Sun square Mars indicates a conflict between your will and drive, potentially leading to impatience or aggressive tendencies.",
        ("Sun", "Jupiter"): "Sun square Jupiter suggests tension between your identity and expansion, potentially leading to overconfidence or unrealistic goals.",
        ("Sun", "Saturn"): "Sun square Saturn indicates tension between your identity and responsibilities, potentially leading to self-doubt or feelings of limitation.",
        ("Sun", "Uranus"): "Sun square Uranus suggests a conflict between your need for self-expression and a desire for freedom, leading to rebellious or unpredictable behavior.",
        ("Sun", "Neptune"): "Sun square Neptune indicates tension between your identity and ideals, potentially leading to confusion or disillusionment.",
        ("Sun", "Pluto"): "Sun square Pluto indicates a powerful drive for transformation and self-mastery. You may face challenges related to control and power struggles but can develop great strength.",
        ("Moon", "Mercury"): "Moon square Mercury suggests tension between emotions and rational thought, potentially leading to misunderstandings or overthinking.",
        ("Moon", "Venus"): "Moon square Venus indicates a conflict between emotions and values, potentially leading to emotional insecurity or challenges in relationships.",
        ("Moon", "Mars"): "Moon square Mars suggests tension between emotions and drive, potentially leading to impulsive reactions or emotional outbursts.",
        ("Moon", "Jupiter"): "Moon square Jupiter indicates a conflict between emotional needs and expansion, potentially leading to overindulgence or unrealistic expectations.",
        ("Moon", "Saturn"): "Moon square Saturn indicates emotional restriction or feelings of inadequacy, requiring patience and self-compassion.",
        ("Moon", "Uranus"): "Moon square Uranus suggests emotional unpredictability and a need for freedom, potentially leading to sudden changes in mood or relationships.",
        ("Moon", "Neptune"): "Moon square Neptune indicates emotional sensitivity and confusion, potentially leading to escapism or idealization.",
        ("Moon", "Pluto"): "Moon square Pluto suggests intense emotional experiences and power struggles, requiring emotional resilience and transformation.",
        ("Mercury", "Venus"): "Mercury square Venus suggests tension between intellect and values, potentially leading to disagreements in relationships or superficial thinking.",
        ("Mercury", "Mars"): "Mercury square Mars indicates a conflict between intellect and drive, potentially leading to argumentative tendencies or hasty decisions.",
        ("Mercury", "Jupiter"): "Mercury square Jupiter suggests tension between detailed thinking and big-picture ideas, potentially leading to scattered thoughts or over-optimism.",
        ("Mercury", "Saturn"): "Mercury square Saturn indicates mental blocks or challenges in communication, requiring discipline and focus to overcome.",
        ("Mercury", "Uranus"): "Mercury square Uranus suggests a conflict between conventional thinking and originality, potentially leading to erratic or rebellious ideas.",
        ("Mercury", "Neptune"): "Mercury square Neptune indicates confusion or deception in communication, requiring clarity and grounding.",
        ("Mercury", "Pluto"): "Mercury square Pluto suggests intense, investigative thinking but may lead to obsessive thoughts or power struggles in communication.",
        ("Venus", "Mars"): "Venus square Mars indicates tension between love and action, potentially leading to passionate conflicts or impulsive attractions.",
        ("Venus", "Jupiter"): "Venus square Jupiter suggests a conflict between love and excess, potentially leading to overindulgence or unrealistic expectations in relationships.",
        ("Venus", "Saturn"): "Venus square Saturn suggests challenges in love and self-worth, potentially leading to feelings of rejection or limitation in relationships.",
        ("Venus", "Uranus"): "Venus square Uranus indicates a conflict between the need for stability in love and a desire for freedom, leading to unpredictable relationships.",
        ("Venus", "Neptune"): "Venus square Neptune suggests idealization or confusion in love, potentially leading to disillusionment or unrealistic expectations.",
        ("Venus", "Pluto"): "Venus square Pluto indicates intense, transformative experiences in love, potentially leading to power struggles or obsession.",
        ("Mars", "Jupiter"): "Mars square Jupiter suggests tension between drive and expansion, potentially leading to overconfidence or reckless actions.",
        ("Mars", "Saturn"): "Mars square Saturn can create internal tension between the desire for action and feelings of restriction or duty. It requires discipline to manage this energy constructively.",
        ("Mars", "Uranus"): "Mars square Uranus suggests impulsive, rebellious actions, potentially leading to accidents or sudden changes.",
        ("Mars", "Neptune"): "Mars square Neptune indicates confusion or misdirected energy, potentially leading to disillusionment or lack of focus.",
        ("Mars", "Pluto"): "Mars square Pluto indicates intense, powerful drives but may lead to conflicts or destructive behavior if not managed carefully.",
        ("Jupiter", "Saturn"): "Jupiter square Saturn suggests tension between expansion and limitation, requiring balance between optimism and realism.",
        ("Jupiter", "Uranus"): "Jupiter square Uranus indicates a conflict between growth and freedom, potentially leading to sudden changes or overextension.",
        ("Jupiter", "Neptune"): "Jupiter square Neptune suggests idealism or over-optimism, potentially leading to disillusionment or lack of practicality.",
        ("Jupiter", "Pluto"): "Jupiter square Pluto suggests a struggle between expansive ambitions and intense power dynamics, requiring balance to avoid excess.",
        ("Saturn", "Uranus"): "Saturn square Uranus indicates tension between tradition and innovation, requiring a balance between stability and change.",
        ("Saturn", "Neptune"): "Saturn square Neptune suggests confusion or challenges in manifesting dreams, requiring grounding and realism.",
        ("Saturn", "Pluto"): "Saturn square Pluto indicates power struggles or intense challenges, requiring discipline and transformation.",
        ("Uranus", "Neptune"): "Uranus square Neptune suggests tension between innovation and spirituality, potentially leading to confusion or disillusionment.",
        ("Uranus", "Pluto"): "Uranus square Pluto indicates revolutionary change and power struggles, requiring adaptability and resilience.",
        ("Neptune", "Pluto"): "Neptune square Pluto suggests deep, transformative spiritual challenges, requiring faith and inner strength.",

        # New entries for MeanNode
        ("Sun", "MeanNode"): "Sun square MeanNode suggests tension between your sense of self and your karmic path. You may face challenges in aligning your individuality and leadership qualities with your life direction.",
        ("Moon", "MeanNode"): "Moon square MeanNode indicates tension between your emotional nature and your karmic path. You may face challenges in developing your intuition and emotional intelligence.",
        ("Mercury", "MeanNode"): "Mercury square MeanNode suggests tension between your communication style and your karmic path. You may face challenges in expressing your ideas and connecting with others in a way that aligns with your life direction.",
        ("Venus", "MeanNode"): "Venus square MeanNode indicates tension between your values, relationships, and creative talents and your karmic path. You may face challenges in developing your sense of beauty and harmony.",
        ("Mars", "MeanNode"): "Mars square MeanNode suggests tension between your drive, assertiveness, and courage and your karmic path. You may face challenges in taking action and pursuing your goals in a way that aligns with your life direction.",
        ("Jupiter", "MeanNode"): "Jupiter square MeanNode indicates tension between your optimism, generosity, and philosophical outlook and your karmic path. You may face challenges in expanding your horizons and seeking wisdom.",
        ("Saturn", "MeanNode"): "Saturn square MeanNode suggests tension between your discipline, responsibility, and structure and your karmic path. You may face challenges in building a solid foundation and achieving your goals through hard work.",
        ("Uranus", "MeanNode"): "Uranus square MeanNode indicates tension between your originality, innovation, and desire for freedom and your karmic path. You may face challenges in embracing change and expressing your unique perspective.",
        ("Neptune", "MeanNode"): "Neptune square MeanNode suggests tension between your intuition, spirituality, and imagination and your karmic path. You may face challenges in developing your compassion and connecting with the divine.",
        ("Pluto", "MeanNode"): "Pluto square MeanNode indicates tension between your intensity, depth, and transformative power and your karmic path. You may face challenges in embracing change and exploring the mysteries of life.",

        # New entries for Ascendant
        ("Sun", "Ascendant"): "Sun square Ascendant suggests tension between your sense of self and your outward personality. You may face challenges in aligning your individuality and leadership qualities with how you present yourself to the world.",
        ("Moon", "Ascendant"): "Moon square Ascendant indicates tension between your emotional nature and your outward personality. You may face challenges in expressing your intuition and emotional intelligence through your personality.",
        ("Mercury", "Ascendant"): "Mercury square Ascendant suggests tension between your communication style and your outward personality. You may face challenges in expressing your ideas and connecting with others through your personality.",
        ("Venus", "Ascendant"): "Venus square Ascendant indicates tension between your values, relationships, and creative talents and your outward personality. You may face challenges in expressing your sense of beauty and harmony through your personality.",
        ("Mars", "Ascendant"): "Mars square Ascendant suggests tension between your drive, assertiveness, and courage and your outward personality. You may face challenges in expressing your energy and competitiveness through your personality.",
        ("Jupiter", "Ascendant"): "Jupiter square Ascendant indicates tension between your optimism, generosity, and philosophical outlook and your outward personality. You may face challenges in expressing your enthusiasm and wisdom through your personality.",
        ("Saturn", "Ascendant"): "Saturn square Ascendant suggests tension between your discipline, responsibility, and structure and your outward personality. You may face challenges in expressing your seriousness and reliability through your personality.",
        ("Uranus", "Ascendant"): "Uranus square Ascendant indicates tension between your originality, innovation, and desire for freedom and your outward personality. You may face challenges in expressing your uniqueness and independence through your personality.",
        ("Neptune", "Ascendant"): "Neptune square Ascendant suggests tension between your intuition, spirituality, and imagination and your outward personality. You may face challenges in expressing your compassion and artistry through your personality.",
        ("Pluto", "Ascendant"): "Pluto square Ascendant indicates tension between your intensity, depth, and transformative power and your outward personality. You may face challenges in expressing your magnetism and power through your personality.",

        # New entries for MidHeaven
        ("Sun", "MidHeaven"): "Sun square MidHeaven suggests tension between your sense of self and your career and public image. You may face challenges in aligning your individuality and leadership qualities with your professional life.",
        ("Moon", "MidHeaven"): "Moon square MidHeaven indicates tension between your emotional nature and your career and public image. You may face challenges in expressing your intuition and emotional intelligence in your professional life.",
        ("Mercury", "MidHeaven"): "Mercury square MidHeaven suggests tension between your communication style and your career and public image. You may face challenges in expressing your ideas and connecting with others in your professional life.",
        ("Venus", "MidHeaven"): "Venus square MidHeaven indicates tension between your values, relationships, and creative talents and your career and public image. You may face challenges in expressing your sense of beauty and harmony in your professional life.",
        ("Mars", "MidHeaven"): "Mars square MidHeaven suggests tension between your drive, assertiveness, and courage and your career and public image. You may face challenges in expressing your energy and competitiveness in your professional life.",
        ("Jupiter", "MidHeaven"): "Jupiter square MidHeaven indicates tension between your optimism, generosity, and philosophical outlook and your career and public image. You may face challenges in expressing your enthusiasm and wisdom in your professional life.",
        ("Saturn", "MidHeaven"): "Saturn square MidHeaven suggests tension between your discipline, responsibility, and structure and your career and public image. You may face challenges in expressing your seriousness and reliability in your professional life.",
        ("Uranus", "MidHeaven"): "Uranus square MidHeaven indicates tension between your originality, innovation, and desire for freedom and your career and public image. You may face challenges in expressing your uniqueness and independence in your professional life.",
        ("Neptune", "MidHeaven"): "Neptune square MidHeaven suggests tension between your intuition, spirituality, and imagination and your career and public image. You may face challenges in expressing your compassion and artistry in your professional life.",
        ("Pluto", "MidHeaven"): "Pluto square MidHeaven indicates tension between your intensity, depth, and transformative power and your career and public image. You may face challenges in expressing your magnetism and power in your professional life."
    },
    "Trine": {
        # Existing planet-planet trines
        ("Sun", "Moon"): "Sun trine Moon indicates harmony between your conscious will and your emotional nature. There is an easy flow between your needs and desires.",
        ("Sun", "Mercury"): "Sun trine Mercury suggests a harmonious blend of identity and intellect, making you clear and confident in communication.",
        ("Sun", "Venus"): "Sun trine Venus indicates a pleasant alignment of identity and values, enhancing your charm and social ease.",
        ("Sun", "Mars"): "Sun trine Mars suggests a harmonious flow of energy between your identity and drive, making you confident and effective.",
        ("Sun", "Jupiter"): "Sun trine Jupiter suggests an easy flow between your identity and growth, bringing optimism, luck, and a sense of purpose.",
        ("Sun", "Saturn"): "Sun trine Saturn indicates a harmonious relationship between your identity and discipline, making you responsible and capable of achieving goals.",
        ("Sun", "Uranus"): "Sun trine Uranus suggests a harmonious blend of your identity and originality, making you innovative and open to change.",
        ("Sun", "Neptune"): "Sun trine Neptune indicates an easy flow between your identity and spirituality, enhancing your intuition and creativity.",
        ("Sun", "Pluto"): "Sun trine Pluto suggests a harmonious relationship between your identity and transformation, making you powerful and capable of deep change.",
        ("Moon", "Mercury"): "Moon trine Mercury indicates a harmonious blend of emotions and intellect, making you intuitive and communicative.",
        ("Moon", "Venus"): "Moon trine Venus suggests a harmonious blend of emotions and affection, making you loving, gentle, and appreciative of beauty.",
        ("Moon", "Mars"): "Moon trine Mars suggests an easy flow between emotions and drive, making you passionate and effective in action.",
        ("Moon", "Jupiter"): "Moon trine Jupiter indicates a harmonious relationship between emotions and growth, bringing optimism and emotional generosity.",
        ("Moon", "Saturn"): "Moon trine Saturn suggests a balance between emotions and discipline, making you emotionally mature and responsible.",
        ("Moon", "Uranus"): "Moon trine Uranus indicates an easy flow between emotions and originality, making you open to change and emotionally independent.",
        ("Moon", "Neptune"): "Moon trine Neptune suggests a harmonious blend of emotions and intuition, enhancing your empathy and imagination.",
        ("Moon", "Pluto"): "Moon trine Pluto indicates a harmonious relationship between emotions and transformation, making you emotionally resilient and deep.",
        ("Mercury", "Venus"): "Mercury trine Venus suggests a pleasant, diplomatic way of communicating, enhancing your social charm and creativity.",
        ("Mercury", "Mars"): "Mercury trine Mars indicates a harmonious blend of intellect and drive, making you quick-witted and effective in communication.",
        ("Mercury", "Jupiter"): "Mercury trine Jupiter suggests a broad-minded, optimistic, and philosophical approach to thinking and communicating. You likely enjoy learning and sharing knowledge.",
        ("Mercury", "Saturn"): "Mercury trine Saturn suggests a balance between intellect and discipline, making you practical and focused in your thinking.",
        ("Mercury", "Uranus"): "Mercury trine Uranus indicates a harmonious relationship between intellect and originality, making you innovative and insightful.",
        ("Mercury", "Neptune"): "Mercury trine Neptune suggests an easy flow between intellect and intuition, enhancing your creativity and imagination.",
        ("Mercury", "Pluto"): "Mercury trine Pluto indicates a harmonious blend of intellect and depth, making you investigative and perceptive.",
        ("Venus", "Mars"): "Venus trine Mars suggests a harmonious relationship between love and action, making you passionate and attractive.",
        ("Venus", "Jupiter"): "Venus trine Jupiter indicates an easy flow between love and growth, bringing luck and generosity in relationships.",
        ("Venus", "Saturn"): "Venus trine Saturn suggests a balance between love and discipline, making you committed and responsible in relationships.",
        ("Venus", "Uranus"): "Venus trine Uranus indicates a harmonious blend of love and originality, making you open to unconventional relationships.",
        ("Venus", "Neptune"): "Venus trine Neptune indicates a romantic, idealistic connection between love and spirituality, enhancing your creativity and compassion.",
        ("Venus", "Pluto"): "Venus trine Pluto suggests a harmonious relationship between love and transformation, making you intense and magnetic in relationships.",
        ("Mars", "Jupiter"): "Mars trine Jupiter suggests a harmonious blend of drive and growth, making you enthusiastic and effective in pursuing goals.",
        ("Mars", "Saturn"): "Mars trine Saturn indicates a balance between drive and discipline, making you persistent and capable of achieving long-term success.",
        ("Mars", "Uranus"): "Mars trine Uranus suggests a dynamic, innovative approach to action, making you effective in pursuing change and freedom.",
        ("Mars", "Neptune"): "Mars trine Neptune indicates a harmonious relationship between drive and intuition, enhancing your spiritual and creative pursuits.",
        ("Mars", "Pluto"): "Mars trine Pluto suggests a harmonious blend of drive and transformation, making you powerful and capable of profound change.",
        ("Jupiter", "Saturn"): "Jupiter trine Saturn suggests a harmonious relationship between expansion and discipline, making you capable of balanced growth.",
        ("Jupiter", "Uranus"): "Jupiter trine Uranus indicates an easy flow between growth and originality, bringing opportunities for innovation and expansion.",
        ("Jupiter", "Neptune"): "Jupiter trine Neptune suggests a harmonious relationship between growth and spirituality, enhancing your faith and compassion.",
        ("Jupiter", "Pluto"): "Jupiter trine Pluto indicates a harmonious blend of growth and transformation, making you capable of profound and expansive change.",
        ("Saturn", "Uranus"): "Saturn trine Uranus suggests a balance between structure and innovation, making you capable of implementing progressive changes.",
        ("Saturn", "Neptune"): "Saturn trine Neptune indicates a harmonious relationship between discipline and intuition, enhancing your ability to manifest dreams.",
        ("Saturn", "Pluto"): "Saturn trine Pluto indicates a powerful ability to transform through discipline, leading to profound and lasting achievements.",
        ("Uranus", "Neptune"): "Uranus trine Neptune suggests a harmonious blend of innovation and spirituality, making you visionary and inspired.",
        ("Uranus", "Pluto"): "Uranus trine Pluto indicates an easy flow between originality and transformation, making you a catalyst for revolutionary change.",
        ("Neptune", "Pluto"): "Neptune trine Pluto suggests a harmonious relationship between intuition and depth, enhancing your spiritual and transformative power.",

        # New entries for MeanNode
        ("Sun", "MeanNode"): "Sun trine MeanNode suggests that your sense of self and purpose harmonizes with your karmic path. You may find it easy to express your individuality and leadership qualities in a way that supports your life direction.",
        ("Moon", "MeanNode"): "Moon trine MeanNode indicates that your emotional nature and nurturing abilities harmonize with your karmic path. You may find it easy to develop your intuition and emotional intelligence.",
        ("Mercury", "MeanNode"): "Mercury trine MeanNode suggests that your communication style and thought processes harmonize with your karmic path. You may find it easy to express your ideas and connect with others in a way that supports your life direction.",
        ("Venus", "MeanNode"): "Venus trine MeanNode indicates that your values, relationships, and creative talents harmonize with your karmic path. You may find it easy to develop your sense of beauty and harmony.",
        ("Mars", "MeanNode"): "Mars trine MeanNode suggests that your drive, assertiveness, and courage harmonize with your karmic path. You may find it easy to take action and pursue your goals in a way that supports your life direction.",
        ("Jupiter", "MeanNode"): "Jupiter trine MeanNode indicates that your optimism, generosity, and philosophical outlook harmonize with your karmic path. You may find it easy to expand your horizons and seek wisdom.",
        ("Saturn", "MeanNode"): "Saturn trine MeanNode suggests that your discipline, responsibility, and structure harmonize with your karmic path. You may find it easy to build a solid foundation and achieve your goals through hard work.",
        ("Uranus", "MeanNode"): "Uranus trine MeanNode indicates that your originality, innovation, and desire for freedom harmonize with your karmic path. You may find it easy to embrace change and express your unique perspective.",
        ("Neptune", "MeanNode"): "Neptune trine MeanNode suggests that your intuition, spirituality, and imagination harmonize with your karmic path. You may find it easy to develop your compassion and connect with the divine.",
        ("Pluto", "MeanNode"): "Pluto trine MeanNode indicates that your intensity, depth, and transformative power harmonize with your karmic path. You may find it easy to embrace change and explore the mysteries of life.",

        # New entries for Ascendant
        ("Sun", "Ascendant"): "Sun trine Ascendant suggests that your sense of self and purpose harmonizes with your outward personality. You may find it easy to express your individuality and leadership qualities through your personality.",
        ("Moon", "Ascendant"): "Moon trine Ascendant indicates that your emotional nature and nurturing abilities harmonize with your outward personality. You may find it easy to express your intuition and emotional intelligence through your personality.",
        ("Mercury", "Ascendant"): "Mercury trine Ascendant suggests that your communication style and thought processes harmonize with your outward personality. You may find it easy to express your ideas and connect with others through your personality.",
        ("Venus", "Ascendant"): "Venus trine Ascendant indicates that your values, relationships, and creative talents harmonize with your outward personality. You may find it easy to express your sense of beauty and harmony through your personality.",
        ("Mars", "Ascendant"): "Mars trine Ascendant suggests that your drive, assertiveness, and courage harmonize with your outward personality. You may find it easy to express your energy and competitiveness through your personality.",
        ("Jupiter", "Ascendant"): "Jupiter trine Ascendant indicates that your optimism, generosity, and philosophical outlook harmonize with your outward personality. You may find it easy to express your enthusiasm and wisdom through your personality.",
        ("Saturn", "Ascendant"): "Saturn trine Ascendant suggests that your discipline, responsibility, and structure harmonize with your outward personality. You may find it easy to express your seriousness and reliability through your personality.",
        ("Uranus", "Ascendant"): "Uranus trine Ascendant indicates that your originality, innovation, and desire for freedom harmonize with your outward personality. You may find it easy to express your uniqueness and independence through your personality.",
        ("Neptune", "Ascendant"): "Neptune trine Ascendant suggests that your intuition, spirituality, and imagination harmonize with your outward personality. You may find it easy to express your compassion and artistry through your personality.",
        ("Pluto", "Ascendant"): "Pluto trine Ascendant indicates that your intensity, depth, and transformative power harmonize with your outward personality. You may find it easy to express your magnetism and power through your personality.",

        # New entries for MidHeaven
        ("Sun", "MidHeaven"): "Sun trine MidHeaven suggests that your sense of self and purpose harmonizes with your career and public image. You may find it easy to express your individuality and leadership qualities in your professional life.",
        ("Moon", "MidHeaven"): "Moon trine MidHeaven indicates that your emotional nature and nurturing abilities harmonize with your career and public image. You may find it easy to express your intuition and emotional intelligence in your professional life.",
        ("Mercury", "MidHeaven"): "Mercury trine MidHeaven suggests that your communication style and thought processes harmonize with your career and public image. You may find it easy to express your ideas and connect with others in your professional life.",
        ("Venus", "MidHeaven"): "Venus trine MidHeaven indicates that your values, relationships, and creative talents harmonize with your career and public image. You may find it easy to express your sense of beauty and harmony in your professional life.",
        ("Mars", "MidHeaven"): "Mars trine MidHeaven suggests that your drive, assertiveness, and courage harmonize with your career and public image. You may find it easy to express your energy and competitiveness in your professional life.",
        ("Jupiter", "MidHeaven"): "Jupiter trine MidHeaven indicates that your optimism, generosity, and philosophical outlook harmonize with your career and public image. You may find it easy to express your enthusiasm and wisdom in your professional life.",
        ("Saturn", "MidHeaven"): "Saturn trine MidHeaven suggests that your discipline, responsibility, and structure harmonize with your career and public image. You may find it easy to express your seriousness and reliability in your professional life.",
        ("Uranus", "MidHeaven"): "Uranus trine MidHeaven indicates that your originality, innovation, and desire for freedom harmonize with your career and public image. You may find it easy to express your uniqueness and independence in your professional life.",
        ("Neptune", "MidHeaven"): "Neptune trine MidHeaven suggests that your intuition, spirituality, and imagination harmonize with your career and public image. You may find it easy to express your compassion and artistry in your professional life.",
        ("Pluto", "MidHeaven"): "Pluto trine MidHeaven indicates that your intensity, depth, and transformative power harmonize with your career and public image. You may find it easy to express your magnetism and power in your professional life."
    },
    "Opposition": {
        # Existing planet-planet oppositions
        ("Sun", "Moon"): "Sun opposition Moon can create tension between your conscious will and your emotional needs. It may manifest as inner conflict or challenges in relationships.",
        ("Sun", "Mercury"): "Sun opposition Mercury suggests tension between your identity and communication, potentially leading to misunderstandings or opposing viewpoints.",
        ("Sun", "Venus"): "Sun opposition Venus indicates a conflict between your identity and values, potentially leading to challenges in relationships or self-expression.",
        ("Sun", "Mars"): "Sun opposition Mars suggests tension between your will and drive, potentially leading to conflicts or competitive struggles.",
        ("Sun", "Jupiter"): "Sun opposition Jupiter indicates a conflict between your identity and expansion, potentially leading to overextension or opposing philosophies.",
        ("Sun", "Saturn"): "Sun opposition Saturn suggests tension between your identity and responsibilities, potentially leading to feelings of limitation or opposition from authority.",
        ("Sun", "Uranus"): "Sun opposition Uranus indicates a conflict between your need for self-expression and a desire for freedom, leading to rebellious or unpredictable behavior.",
        ("Sun", "Neptune"): "Sun opposition Neptune suggests tension between your identity and ideals, potentially leading to confusion or disillusionment.",
        ("Sun", "Pluto"): "Sun opposition Pluto indicates power struggles or intense challenges related to control and transformation, requiring balance and awareness.",
        ("Moon", "Mercury"): "Moon opposition Mercury suggests tension between emotions and intellect, potentially leading to emotional misunderstandings or overanalyzing feelings.",
        ("Moon", "Venus"): "Moon opposition Venus indicates a conflict between emotions and values, potentially leading to emotional insecurity or relational tension.",
        ("Moon", "Mars"): "Moon opposition Mars suggests tension between emotions and drive, potentially leading to emotional conflicts or impulsive reactions.",
        ("Moon", "Jupiter"): "Moon opposition Jupiter indicates a conflict between emotional needs and expansion, potentially leading to emotional excess or unrealistic expectations.",
        ("Moon", "Saturn"): "Moon opposition Saturn suggests emotional restriction or feelings of inadequacy, requiring patience and self-compassion.",
        ("Moon", "Uranus"): "Moon opposition Uranus indicates emotional unpredictability and a need for freedom, potentially leading to sudden changes in mood or relationships.",
        ("Moon", "Neptune"): "Moon opposition Neptune suggests emotional sensitivity and confusion, potentially leading to escapism or idealization.",
        ("Moon", "Pluto"): "Moon opposition Pluto indicates intense emotional experiences and power struggles, requiring emotional resilience and transformation.",
        ("Mercury", "Venus"): "Mercury opposition Venus suggests tension between intellect and values, potentially leading to disagreements in relationships or differing priorities.",
        ("Mercury", "Mars"): "Mercury opposition Mars indicates a conflict between intellect and drive, potentially leading to arguments or hasty communication.",
        ("Mercury", "Jupiter"): "Mercury opposition Jupiter suggests tension between detailed thinking and big-picture ideas, potentially leading to overconfidence or scattered thoughts.",
        ("Mercury", "Saturn"): "Mercury opposition Saturn suggests a tension between free thought and restriction, potentially leading to self-doubt or serious contemplation.",
        ("Mercury", "Uranus"): "Mercury opposition Uranus indicates a conflict between conventional thinking and originality, potentially leading to erratic or rebellious ideas.",
        ("Mercury", "Neptune"): "Mercury opposition Neptune suggests confusion or deception in communication, requiring clarity and grounding.",
        ("Mercury", "Pluto"): "Mercury opposition Pluto indicates intense, investigative thinking but may lead to obsessive thoughts or power struggles in communication.",
        ("Venus", "Mars"): "Venus opposition Mars suggests tension between love and action, potentially leading to passionate conflicts or opposing desires.",
        ("Venus", "Jupiter"): "Venus opposition Jupiter indicates a conflict between indulgence and excess in love or pleasure, requiring moderation for harmony.",
        ("Venus", "Saturn"): "Venus opposition Saturn suggests challenges in love and self-worth, potentially leading to feelings of rejection or limitation in relationships.",
        ("Venus", "Uranus"): "Venus opposition Uranus indicates a conflict between the need for stability in love and a desire for freedom, leading to unpredictable relationships.",
        ("Venus", "Neptune"): "Venus opposition Neptune suggests idealization or confusion in love, potentially leading to disillusionment or unrealistic expectations.",
        ("Venus", "Pluto"): "Venus opposition Pluto indicates intense, transformative experiences in love, potentially leading to power struggles or obsession.",
        ("Mars", "Jupiter"): "Mars opposition Jupiter suggests tension between drive and expansion, potentially leading to overconfidence or reckless actions.",
        ("Mars", "Saturn"): "Mars opposition Saturn indicates tension between action and restriction, potentially leading to frustration or delays.",
        ("Mars", "Uranus"): "Mars opposition Uranus suggests impulsive, rebellious actions, potentially leading to accidents or sudden changes.",
        ("Mars", "Neptune"): "Mars opposition Neptune indicates confusion or misdirected energy, potentially leading to disillusionment or lack of focus.",
        ("Mars", "Pluto"): "Mars opposition Pluto indicates intense power struggles and the need to transform your approach to conflict. It requires awareness to avoid manipulation.",
        ("Jupiter", "Saturn"): "Jupiter opposition Saturn suggests tension between expansion and limitation, requiring balance between optimism and realism.",
        ("Jupiter", "Uranus"): "Jupiter opposition Uranus indicates a conflict between growth and freedom, potentially leading to sudden changes or overextension.",
        ("Jupiter", "Neptune"): "Jupiter opposition Neptune suggests idealism or over-optimism, potentially leading to disillusionment or lack of practicality.",
        ("Jupiter", "Pluto"): "Jupiter opposition Pluto indicates a struggle between expansive ambitions and intense power dynamics, requiring balance to avoid excess.",
        ("Saturn", "Uranus"): "Saturn opposition Uranus suggests tension between tradition and innovation, requiring a balance between stability and change.",
        ("Saturn", "Neptune"): "Saturn opposition Neptune indicates confusion or challenges in manifesting dreams, requiring grounding and realism.",
        ("Saturn", "Pluto"): "Saturn opposition Pluto suggests power struggles or intense challenges, requiring discipline and transformation.",
        ("Uranus", "Neptune"): "Uranus opposition Neptune indicates tension between innovation and spirituality, potentially leading to confusion or disillusionment.",
        ("Uranus", "Pluto"): "Uranus opposition Pluto suggests a dramatic tension between revolutionary change and deep transformation, leading to significant shifts.",
        ("Neptune", "Pluto"): "Neptune opposition Pluto indicates deep, transformative spiritual challenges, requiring faith and inner strength.",

        # New entries for MeanNode
        ("Sun", "MeanNode"): "Sun opposition MeanNode suggests a need to balance your sense of self and purpose with your karmic path. You may encounter conflicts or challenges that require you to integrate your individuality and leadership qualities with your life direction.",
        ("Moon", "MeanNode"): "Moon opposition MeanNode indicates a need to balance your emotional nature and nurturing abilities with your karmic path. You may encounter conflicts or challenges that require you to integrate your intuition and emotional intelligence with your life direction.",
        ("Mercury", "MeanNode"): "Mercury opposition MeanNode suggests a need to balance your communication style and thought processes with your karmic path. You may encounter conflicts or challenges that require you to integrate your ideas and connections with your life direction.",
        ("Venus", "MeanNode"): "Venus opposition MeanNode indicates a need to balance your values, relationships, and creative talents with your karmic path. You may encounter conflicts or challenges that require you to integrate your sense of beauty and harmony with your life direction.",
        ("Mars", "MeanNode"): "Mars opposition MeanNode suggests a need to balance your drive, assertiveness, and courage with your karmic path. You may encounter conflicts or challenges that require you to integrate your actions and goals with your life direction.",
        ("Jupiter", "MeanNode"): "Jupiter opposition MeanNode indicates a need to balance your optimism, generosity, and philosophical outlook with your karmic path. You may encounter conflicts or challenges that require you to integrate your expansion and wisdom with your life direction.",
        ("Saturn", "MeanNode"): "Saturn opposition MeanNode suggests a need to balance your discipline, responsibility, and structure with your karmic path. You may encounter conflicts or challenges that require you to integrate your foundation and achievements with your life direction.",
        ("Uranus", "MeanNode"): "Uranus opposition MeanNode indicates a need to balance your originality, innovation, and desire for freedom with your karmic path. You may encounter conflicts or challenges that require you to integrate your change and perspective with your life direction.",
        ("Neptune", "MeanNode"): "Neptune opposition MeanNode suggests a need to balance your intuition, spirituality, and imagination with your karmic path. You may encounter conflicts or challenges that require you to integrate your compassion and connection with your life direction.",
        ("Pluto", "MeanNode"): "Pluto opposition MeanNode indicates a need to balance your intensity, depth, and transformative power with your karmic path. You may encounter conflicts or challenges that require you to integrate your change and exploration with your life direction.",

        # New entries for Ascendant
        ("Sun", "Ascendant"): "Sun opposition Ascendant suggests a need to balance your sense of self and purpose with your outward personality. You may encounter conflicts or challenges that require you to integrate your individuality and leadership qualities with how you present yourself to the world.",
        ("Moon", "Ascendant"): "Moon opposition Ascendant indicates a need to balance your emotional nature and nurturing abilities with your outward personality. You may encounter conflicts or challenges that require you to integrate your intuition and emotional intelligence with how you present yourself to the world.",
        ("Mercury", "Ascendant"): "Mercury opposition Ascendant suggests a need to balance your communication style and thought processes with your outward personality. You may encounter conflicts or challenges that require you to integrate your ideas and connections with how you present yourself to the world.",
        ("Venus", "Ascendant"): "Venus opposition Ascendant indicates a need to balance your values, relationships, and creative talents with your outward personality. You may encounter conflicts or challenges that require you to integrate your sense of beauty and harmony with how you present yourself to the world.",
        ("Mars", "Ascendant"): "Mars opposition Ascendant suggests a need to balance your drive, assertiveness, and courage with your outward personality. You may encounter conflicts or challenges that require you to integrate your actions and goals with how you present yourself to the world.",
        ("Jupiter", "Ascendant"): "Jupiter opposition Ascendant indicates a need to balance your optimism, generosity, and philosophical outlook with your outward personality. You may encounter conflicts or challenges that require you to integrate your expansion and wisdom with how you present yourself to the world.",
        ("Saturn", "Ascendant"): "Saturn opposition Ascendant suggests a need to balance your discipline, responsibility, and structure with your outward personality. You may encounter conflicts or challenges that require you to integrate your foundation and achievements with how you present yourself to the world.",
        ("Uranus", "Ascendant"): "Uranus opposition Ascendant indicates a need to balance your originality, innovation, and desire for freedom with your outward personality. You may encounter conflicts or challenges that require you to integrate your change and perspective with how you present yourself to the world.",
        ("Neptune", "Ascendant"): "Neptune opposition Ascendant suggests a need to balance your intuition, spirituality, and imagination with your outward personality. You may encounter conflicts or challenges that require you to integrate your compassion and connection with how you present yourself to the world.",
        ("Pluto", "Ascendant"): "Pluto opposition Ascendant indicates a need to balance your intensity, depth, and transformative power with your outward personality. You may encounter conflicts or challenges that require you to integrate your change and exploration with how you present yourself to the world.",

        # New entries for MidHeaven
        ("Sun", "MidHeaven"): "Sun opposition MidHeaven suggests a need to balance your sense of self and purpose with your career and public image. You may encounter conflicts or challenges that require you to integrate your individuality and leadership qualities with your professional life.",
        ("Moon", "MidHeaven"): "Moon opposition MidHeaven indicates a need to balance your emotional nature and nurturing abilities with your career and public image. You may encounter conflicts or challenges that require you to integrate your intuition and emotional intelligence with your professional life.",
        ("Mercury", "MidHeaven"): "Mercury opposition MidHeaven suggests a need to balance your communication style and thought processes with your career and public image. You may encounter conflicts or challenges that require you to integrate your ideas and connections with your professional life.",
        ("Venus", "MidHeaven"): "Venus opposition MidHeaven indicates a need to balance your values, relationships, and creative talents with your career and public image. You may encounter conflicts or challenges that require you to integrate your sense of beauty and harmony with your professional life.",
        ("Mars", "MidHeaven"): "Mars opposition MidHeaven suggests a need to balance your drive, assertiveness, and courage with your career and public image. You may encounter conflicts or challenges that require you to integrate your actions and goals with your professional life.",
        ("Jupiter", "MidHeaven"): "Jupiter opposition MidHeaven indicates a need to balance your optimism, generosity, and philosophical outlook with your career and public image. You may encounter conflicts or challenges that require you to integrate your expansion and wisdom with your professional life.",
        ("Saturn", "MidHeaven"): "Saturn opposition MidHeaven suggests a need to balance your discipline, responsibility, and structure with your career and public image. You may encounter conflicts or challenges that require you to integrate your foundation and achievements with your professional life.",
        ("Uranus", "MidHeaven"): "Uranus opposition MidHeaven indicates a need to balance your originality, innovation, and desire for freedom with your career and public image. You may encounter conflicts or challenges that require you to integrate your change and perspective with your professional life.",
        ("Neptune", "MidHeaven"): "Neptune opposition MidHeaven suggests a need to balance your intuition, spirituality, and imagination with your career and public image. You may encounter conflicts or challenges that require you to integrate your compassion and connection with your professional life.",
        ("Pluto", "MidHeaven"): "Pluto opposition MidHeaven indicates a need to balance your intensity, depth, and transformative power with your career and public image. You may encounter conflicts or challenges that require you to integrate your change and exploration with your professional life."
    }
}

HOUSE_CUSP_SIGN_INTERPRETATIONS = {
    1: {
        "Aries": "Aries on the cusp of the 1st house (Ascendant) gives a direct, energetic, and assertive approach to new beginnings and how you meet the world.",
        "Taurus": "Taurus on the cusp of the 1st house (Ascendant) gives a steady, reliable, and sensual approach to new beginnings and how you meet the world.",
        "Gemini": "Gemini on the cusp of the 1st house (Ascendant) suggests a curious, adaptable, and communicative approach to life. You are likely versatile and enjoy learning.",
        "Cancer": "Cancer on the cusp of the 1st house (Ascendant) indicates a nurturing, protective, and emotional approach to self-expression. You are likely intuitive and value security.",
        "Leo": "Leo on the cusp of the 1st house (Ascendant) gives a confident, creative, and dramatic flair to your personality. You are likely charismatic and enjoy being noticed.",
        "Virgo": "Virgo on the cusp of the 1st house (Ascendant) suggests a practical, analytical, and detail-oriented approach to life. You are likely modest and strive for improvement.",
        "Libra": "Libra on the cusp of the 1st house (Ascendant) indicates a diplomatic, harmonious, and relationship-focused approach to self-expression. You are likely charming and value balance.",
        "Scorpio": "Scorpio on the cusp of the 1st house (Ascendant) gives an intense, mysterious, and transformative quality to your personality. You are likely passionate and not afraid of depth.",
        "Sagittarius": "Sagittarius on the cusp of the 1st house (Ascendant) suggests an adventurous, optimistic, and philosophical approach to life. You are likely enthusiastic and enjoy exploration.",
        "Capricorn": "Capricorn on the cusp of the 1st house (Ascendant) indicates a disciplined, responsible, and ambitious approach to self-expression. You are likely practical and goal-oriented.",
        "Aquarius": "Aquarius on the cusp of the 1st house (Ascendant) gives an innovative, independent, and humanitarian quality to your personality. You are likely original and value freedom.",
        "Pisces": "Pisces on the cusp of the 1st house (Ascendant) suggests a compassionate, imaginative, and sensitive approach to life. You are likely intuitive and artistic."
    },
    2: {
        "Aries": "Aries on the cusp of the 2nd house suggests an energetic, impulsive approach to finances and values. You are likely proactive in building resources.",
        "Taurus": "Taurus on the cusp of the 2nd house indicates a steady, sensual approach to money and possessions. You are likely focused on comfort and security.",
        "Gemini": "Gemini on the cusp of the 2nd house points to a versatile, intellectual approach to resources. You may earn through communication or multiple sources.",
        "Cancer": "Cancer on the cusp of the 2nd house suggests an emotional, nurturing approach to finances. You are likely protective of your resources.",
        "Leo": "Leo on the cusp of the 2nd house indicates a generous, dramatic approach to money and values. You are likely proud of your possessions.",
        "Virgo": "Virgo on the cusp of the 2nd house suggests a practical, detail-oriented approach to finances. You are likely frugal and value efficiency.",
        "Libra": "Libra on the cusp of the 2nd house indicates a harmonious, aesthetic approach to resources. You are likely drawn to beauty and balance in spending.",
        "Scorpio": "Scorpio on the cusp of the 2nd house suggests an intense, transformative approach to money. You are likely resourceful and secretive about finances.",
        "Sagittarius": "Sagittarius on the cusp of the 2nd house points to an adventurous, optimistic approach to resources. You may spend on travel or learning.",
        "Capricorn": "Capricorn on the cusp of the 2nd house indicates a disciplined, ambitious approach to finances. You are likely focused on long-term security.",
        "Aquarius": "Aquarius on the cusp of the 2nd house suggests an unconventional, innovative approach to money. You may value freedom over material wealth.",
        "Pisces": "Pisces on the cusp of the 2nd house indicates a compassionate, intuitive approach to resources. You may be generous or idealistic about money."
    },
    3: {
        "Aries": "Aries on the cusp of the 3rd house suggests a bold, assertive communication style. You are likely direct and enjoy intellectual challenges.",
        "Taurus": "Taurus on the cusp of the 3rd house indicates a steady, practical approach to learning and communication. You are likely deliberate in your words.",
        "Gemini": "Gemini on the cusp of the 3rd house points to a curious, versatile, and communicative nature. You are likely quick-witted and sociable.",
        "Cancer": "Cancer on the cusp of the 3rd house suggests an emotional, intuitive approach to communication. You are likely sensitive in conversations.",
        "Leo": "Leo on the cusp of the 3rd house indicates a confident, dramatic communication style. You are likely expressive and enjoy attention.",
        "Virgo": "Virgo on the cusp of the 3rd house suggests a precise, analytical approach to learning. You are likely detail-oriented and practical.",
        "Libra": "Libra on the cusp of the 3rd house indicates a diplomatic, harmonious communication style. You are likely charming and balanced.",
        "Scorpio": "Scorpio on the cusp of the 3rd house suggests an intense, probing approach to communication. You are likely deep and investigative.",
        "Sagittarius": "Sagittarius on the cusp of the 3rd house points to an adventurous, philosophical approach to learning. You are likely broad-minded.",
        "Capricorn": "Capricorn on the cusp of the 3rd house indicates a serious, structured approach to communication. You are likely strategic and reserved.",
        "Aquarius": "Aquarius on the cusp of the 3rd house suggests an innovative, original communication style. You are likely progressive and unique.",
        "Pisces": "Pisces on the cusp of the 3rd house indicates an imaginative, intuitive approach to learning. You are likely poetic and empathetic."
    },
    4: {
        "Aries": "Aries on the cusp of the 4th house suggests an energetic, independent approach to home and family. You are likely proactive in your domestic life.",
        "Taurus": "Taurus on the cusp of the 4th house indicates a stable, comforting approach to home. You are likely focused on creating a secure environment.",
        "Gemini": "Gemini on the cusp of the 4th house points to a communicative, adaptable approach to family. You may enjoy a lively home life.",
        "Cancer": "Cancer on the cusp of the 4th house suggests a nurturing, emotional connection to home. You are likely protective and family-oriented.",
        "Leo": "Leo on the cusp of the 4th house indicates a proud, creative approach to home life. You are likely warm and enjoy a dramatic flair.",
        "Virgo": "Virgo on the cusp of the 4th house suggests a practical, organized approach to home. You are likely focused on order and efficiency.",
        "Libra": "Libra on the cusp of the 4th house indicates a harmonious, aesthetic approach to family life. You are likely peace-loving at home.",
        "Scorpio": "Scorpio on the cusp of the 4th house suggests an intense, private approach to home. You are likely deep and protective of your roots.",
        "Sagittarius": "Sagittarius on the cusp of the 4th house points to an adventurous, open approach to home. You may value freedom in your domestic life.",
        "Capricorn": "Capricorn on the cusp of the 4th house indicates a disciplined, traditional approach to family. You are likely responsible and structured.",
        "Aquarius": "Aquarius on the cusp of the 4th house suggests an unconventional, progressive approach to home. You are likely innovative in your domestic life.",
        "Pisces": "Pisces on the cusp of the 4th house indicates a compassionate, dreamy approach to family. You are likely intuitive and nurturing."
    },
    5: {
        "Aries": "Aries on the cusp of the 5th house suggests a bold, passionate approach to creativity and romance. You are likely competitive and spontaneous.",
        "Taurus": "Taurus on the cusp of the 5th house indicates a sensual, steady approach to pleasure. You are likely drawn to beauty and comfort in love.",
        "Gemini": "Gemini on the cusp of the 5th house points to a playful, intellectual approach to creativity. You are likely versatile and enjoy variety.",
        "Cancer": "Cancer on the cusp of the 5th house suggests an emotional, nurturing approach to romance. You are likely affectionate and protective.",
        "Leo": "Leo on the cusp of the 5th house indicates a dramatic, confident approach to self-expression. You are likely creative and seek attention.",
        "Virgo": "Virgo on the cusp of the 5th house suggests a practical, detailed approach to creativity. You are likely modest and service-oriented.",
        "Libra": "Libra on the cusp of the 5th house indicates a harmonious, romantic approach to pleasure. You are likely charming and value balance.",
        "Scorpio": "Scorpio on the cusp of the 5th house suggests an intense, passionate approach to love. You are likely deep and transformative.",
        "Sagittarius": "Sagittarius on the cusp of the 5th house points to an adventurous, optimistic approach to creativity. You are likely enthusiastic and free-spirited.",
        "Capricorn": "Capricorn on the cusp of the 5th house indicates a disciplined, serious approach to pleasure. You are likely goal-oriented in romance.",
        "Aquarius": "Aquarius on the cusp of the 5th house suggests an unconventional, innovative approach to creativity. You are likely original and detached.",
        "Pisces": "Pisces on the cusp of the 5th house indicates a dreamy, compassionate approach to love. You are likely artistic and romantic."
    },
    6: {
        "Aries": "Aries on the cusp of the 6th house suggests an energetic, assertive approach to work and health. You are likely proactive and driven.",
        "Taurus": "Taurus on the cusp of the 6th house indicates a steady, practical approach to daily routines. You are likely reliable and focused on well-being.",
        "Gemini": "Gemini on the cusp of the 6th house points to a versatile, communicative approach to work. You are likely adaptable and mentally active.",
        "Cancer": "Cancer on the cusp of the 6th house suggests a nurturing, caring approach to health and service. You are likely empathetic and protective.",
        "Leo": "Leo on the cusp of the 6th house indicates a confident, creative approach to work. You are likely proud and seek recognition in service.",
        "Virgo": "Virgo on the cusp of the 6th house suggests a precise, analytical approach to routines. You are likely efficient and detail-oriented.",
        "Libra": "Libra on the cusp of the 6th house indicates a harmonious, balanced approach to work. You are likely diplomatic and value fairness.",
        "Scorpio": "Scorpio on the cusp of the 6th house suggests an intense, focused approach to health and service. You are likely deep and determined.",
        "Sagittarius": "Sagittarius on the cusp of the 6th house points to an optimistic, expansive approach to work. You are likely adventurous and philosophical.",
        "Capricorn": "Capricorn on the cusp of the 6th house indicates a disciplined, responsible approach to routines. You are likely hardworking and structured.",
        "Aquarius": "Aquarius on the cusp of the 6th house suggests an innovative, unconventional approach to work. You are likely progressive and independent.",
        "Pisces": "Pisces on the cusp of the 6th house indicates a compassionate, intuitive approach to service. You are likely gentle and spiritually inclined."
    },
    7: {
        "Aries": "Aries on the cusp of the 7th house suggests a dynamic, assertive approach to partnerships. You are likely drawn to strong, independent individuals.",
        "Taurus": "Taurus on the cusp of the 7th house indicates a stable, loyal approach to relationships. You are likely attracted to security and comfort.",
        "Gemini": "Gemini on the cusp of the 7th house points to a communicative, versatile approach to partnerships. You are likely intellectual and sociable.",
        "Cancer": "Cancer on the cusp of the 7th house suggests an emotional, nurturing approach to relationships. You are likely caring and seek emotional bonds.",
        "Leo": "Leo on the cusp of the 7th house indicates a dramatic, generous approach to partnerships. You are likely warm and seek admiration.",
        "Virgo": "Virgo on the cusp of the 7th house suggests a practical, service-oriented approach to relationships. You are likely helpful and detail-focused.",
        "Libra": "Libra on the cusp of the 7th house indicates a harmonious, balanced approach to partnerships. You are likely romantic and value equality.",
        "Scorpio": "Scorpio on the cusp of the 7th house suggests an intense, passionate approach to relationships. You are likely deep and transformative.",
        "Sagittarius": "Sagittarius on the cusp of the 7th house points to an adventurous, open-minded approach to partnerships. You are likely free-spirited.",
        "Capricorn": "Capricorn on the cusp of the 7th house indicates a serious, committed approach to relationships. You are likely responsible and traditional.",
        "Aquarius": "Aquarius on the cusp of the 7th house suggests an unconventional, independent approach to partnerships. You are likely progressive and detached.",
        "Pisces": "Pisces on the cusp of the 7th house indicates a compassionate, romantic approach to relationships. You are likely empathetic and dreamy."
    },
    8: {
        "Aries": "Aries on the cusp of the 8th house suggests a bold, fearless approach to transformation and shared resources. You are likely intense and proactive.",
        "Taurus": "Taurus on the cusp of the 8th house indicates a steady, sensual approach to intimacy and finances. You are likely possessive and value security.",
        "Gemini": "Gemini on the cusp of the 8th house points to a curious, communicative approach to mysteries. You are likely intellectual and adaptable.",
        "Cancer": "Cancer on the cusp of the 8th house suggests an emotional, protective approach to transformation. You are likely intuitive and deep.",
        "Leo": "Leo on the cusp of the 8th house indicates a dramatic, powerful approach to shared resources. You are likely proud and seek control.",
        "Virgo": "Virgo on the cusp of the 8th house suggests a practical, analytical approach to intimacy. You are likely cautious and detail-oriented.",
        "Libra": "Libra on the cusp of the 8th house indicates a harmonious, balanced approach to transformation. You are likely diplomatic and seek fairness.",
        "Scorpio": "Scorpio on the cusp of the 8th house suggests an intense, transformative approach to life’s mysteries. You are likely passionate and resourceful.",
        "Sagittarius": "Sagittarius on the cusp of the 8th house points to an adventurous, philosophical approach to depth. You are likely open to change.",
        "Capricorn": "Capricorn on the cusp of the 8th house indicates a disciplined, strategic approach to shared resources. You are likely serious and controlled.",
        "Aquarius": "Aquarius on the cusp of the 8th house suggests an unconventional, innovative approach to transformation. You are likely detached and visionary.",
        "Pisces": "Pisces on the cusp of the 8th house indicates a compassionate, spiritual approach to intimacy. You are likely intuitive and mystical."
    },
    9: {
        "Aries": "Aries on the cusp of the 9th house suggests a bold, pioneering approach to learning and exploration. You are likely enthusiastic and direct.",
        "Taurus": "Taurus on the cusp of the 9th house indicates a steady, practical approach to philosophy and travel. You are likely grounded and value beauty.",
        "Gemini": "Gemini on the cusp of the 9th house points to a curious, communicative approach to higher learning. You are likely versatile and intellectual.",
        "Cancer": "Cancer on the cusp of the 9th house suggests an emotional, intuitive approach to beliefs. You are likely nurturing and tied to tradition.",
        "Leo": "Leo on the cusp of the 9th house indicates a confident, dramatic approach to exploration. You are likely proud and seek recognition.",
        "Virgo": "Virgo on the cusp of the 9th house suggests a practical, analytical approach to philosophy. You are likely detail-oriented and service-minded.",
        "Libra": "Libra on the cusp of the 9th house indicates a harmonious, balanced approach to learning. You are likely diplomatic and value justice.",
        "Scorpio": "Scorpio on the cusp of the 9th house suggests an intense, transformative approach to beliefs. You are likely deep and investigative.",
        "Sagittarius": "Sagittarius on the cusp of the 9th house points to an adventurous, optimistic approach to exploration. You are likely philosophical and free.",
        "Capricorn": "Capricorn on the cusp of the 9th house indicates a disciplined, ambitious approach to learning. You are likely serious and goal-oriented.",
        "Aquarius": "Aquarius on the cusp of the 9th house suggests an innovative, progressive approach to philosophy. You are likely original and humanitarian.",
        "Pisces": "Pisces on the cusp of the 9th house indicates a compassionate, spiritual approach to exploration. You are likely intuitive and dreamy."
    },
    10: {
        "Aries": "Aries on the cusp of the 10th house (Midheaven) suggests a pioneering, assertive, and leadership-oriented approach to career and public life.",
        "Taurus": "Taurus on the cusp of the 10th house (Midheaven) indicates a steady, persistent, and value-driven approach to your professional goals.",
        "Gemini": "Gemini on the cusp of the 10th house (Midheaven) points to a versatile, communicative, and intellectually stimulating career path.",
        "Cancer": "Cancer on the cusp of the 10th house (Midheaven) suggests a nurturing, protective, and family-oriented approach to your public image and career.",
        "Leo": "Leo on the cusp of the 10th house (Midheaven) indicates a desire for recognition, creativity, and leadership in your professional life.",
        "Virgo": "Virgo on the cusp of the 10th house (Midheaven) points to a detail-oriented, service-focused, and analytical approach to your career.",
        "Libra": "Libra on the cusp of the 10th house (Midheaven) suggests a diplomatic, harmonious, and partnership-oriented approach to your public life.",
        "Scorpio": "Scorpio on the cusp of the 10th house (Midheaven) indicates an intense, transformative, and powerful approach to your career and public image.",
        "Sagittarius": "Sagittarius on the cusp of the 10th house (Midheaven) points to an adventurous, philosophical, and expansive approach to your professional goals.",
        "Capricorn": "Capricorn on the cusp of the 10th house (Midheaven) suggests a disciplined, responsible, and ambitious approach to career and public life.",
        "Aquarius": "Aquarius on the cusp of the 10th house (Midheaven) suggests an innovative, humanitarian, and unconventional approach to your career.",
        "Pisces": "Pisces on the cusp of the 10th house (Midheaven) indicates a compassionate, artistic, and spiritually-oriented approach to your public life."
    },
    11: {
        "Aries": "Aries on the cusp of the 11th house suggests a bold, independent approach to friendships and goals. You are likely a leader in groups.",
        "Taurus": "Taurus on the cusp of the 11th house indicates a steady, loyal approach to social connections. You are likely reliable and value comfort.",
        "Gemini": "Gemini on the cusp of the 11th house points to a communicative, versatile approach to friendships. You are likely sociable and curious.",
        "Cancer": "Cancer on the cusp of the 11th house suggests an emotional, nurturing approach to groups. You are likely caring and seek emotional ties.",
        "Leo": "Leo on the cusp of the 11th house indicates a confident, generous approach to friendships. You are likely warm and seek recognition.",
        "Virgo": "Virgo on the cusp of the 11th house suggests a practical, service-oriented approach to goals. You are likely helpful and detail-focused.",
        "Libra": "Libra on the cusp of the 11th house indicates a harmonious, balanced approach to social life. You are likely charming and value equality.",
        "Scorpio": "Scorpio on the cusp of the 11th house suggests an intense, transformative approach to friendships. You are likely deep and selective.",
        "Sagittarius": "Sagittarius on the cusp of the 11th house points to an adventurous, optimistic approach to groups. You are likely enthusiastic and free.",
        "Capricorn": "Capricorn on the cusp of the 11th house indicates a disciplined, ambitious approach to goals. You are likely serious and structured.",
        "Aquarius": "Aquarius on the cusp of the 11th house suggests an innovative, progressive approach to friendships. You are likely original and humanitarian.",
        "Pisces": "Pisces on the cusp of the 11th house indicates a compassionate, dreamy approach to social causes. You are likely empathetic and idealistic."
    },
    12: {
        "Aries": "Aries on the cusp of the 12th house suggests a bold, hidden drive for independence. You are likely assertive in private or spiritual matters.",
        "Taurus": "Taurus on the cusp of the 12th house indicates a steady, sensual approach to the subconscious. You are likely grounded but secretive.",
        "Gemini": "Gemini on the cusp of the 12th house points to a curious, communicative approach to hidden matters. You are likely introspective and mental.",
        "Cancer": "Cancer on the cusp of the 12th house suggests an emotional, nurturing approach to spirituality. You are likely intuitive and private.",
        "Leo": "Leo on the cusp of the 12th house indicates a confident, dramatic approach to the subconscious. You are likely creative in solitude.",
        "Virgo": "Virgo on the cusp of the 12th house suggests a practical, analytical approach to hidden matters. You are likely detail-oriented and introspective.",
        "Libra": "Libra on the cusp of the 12th house indicates a harmonious, balanced approach to spirituality. You are likely peace-seeking in private.",
        "Scorpio": "Scorpio on the cusp of the 12th house suggests an intense, transformative approach to the subconscious. You are likely deep and mysterious.",
        "Sagittarius": "Sagittarius on the cusp of the 12th house points to an adventurous, philosophical approach to spirituality. You are likely optimistic and expansive.",
        "Capricorn": "Capricorn on the cusp of the 12th house indicates a disciplined, serious approach to hidden matters. You are likely responsible and reserved.",
        "Aquarius": "Aquarius on the cusp of the 12th house suggests an innovative, progressive approach to the subconscious. You are likely original and detached.",
        "Pisces": "Pisces on the cusp of the 12th house indicates a compassionate, spiritual approach to hidden matters. You are likely intuitive and dreamy."
    }
}


class InterpretationGenerator:
    def __init__(self):
        pass

    def get_planet_in_sign_interpretation(self, planet_name, sign_name):
        return PLANET_IN_SIGN_INTERPRETATIONS.get(planet_name, {}).get(sign_name, f"No specific interpretation for {planet_name} in {sign_name} available yet.")

    def get_planet_in_house_interpretation(self, planet_name, house_number):
        if not isinstance(house_number, int):
            return f"Invalid house number for {planet_name}."
        return PLANET_IN_HOUSE_INTERPRETATIONS.get(planet_name, {}).get(house_number, f"No specific interpretation for {planet_name} in House {house_number} available yet.")

    def get_aspect_interpretation(self, body1_name, body2_name, aspect_type):
        # Ensure consistent order for lookup
        # key_pair = tuple(sorted((body1_name, body2_name)))
        key_pair = tuple((body1_name, body2_name))
        print(key_pair)
        return ASPECT_INTERPRETATIONS.get(aspect_type, {}).get(key_pair, f"No specific interpretation for {body1_name} {aspect_type} {body2_name} available yet.")

    def get_house_cusp_interpretation(self, house_number, sign_name):
        if not isinstance(house_number, int):
            return f"Invalid house number for cusp interpretation."
        return HOUSE_CUSP_SIGN_INTERPRETATIONS.get(house_number, {}).get(sign_name, f"No specific interpretation for House {house_number} cusp in {sign_name} available yet.")

    def generate_full_interpretation(self, chart_data):
        """Generates a list of interpretations from the chart data."""
        if not chart_data or not isinstance(chart_data, dict):
            return {"error": "Invalid chart data provided."}

        interpretations = {
            "planets_in_signs": [],
            "planets_in_houses": [],
            "aspects": [],
            "house_cusps": []
        }

        # Planet in Sign and Planet in House
        for planet_data in chart_data.get("planets", []):
            p_name = planet_data.get("name")
            p_sign = planet_data.get("sign")
            p_house = planet_data.get("house_number")

            if p_name and p_sign:
                interp_sign = self.get_planet_in_sign_interpretation(p_name, p_sign)
                interpretations["planets_in_signs"].append(f"{p_name} in {p_sign}: {interp_sign}")
            
            if p_name and p_house is not None:
                interp_house = self.get_planet_in_house_interpretation(p_name, p_house)
                interpretations["planets_in_houses"].append(f"{p_name} in House {p_house}: {interp_house}")
        
        # Aspects
        for aspect_data in chart_data.get("aspects", []):
            b1 = aspect_data.get("body1")
            b2 = aspect_data.get("body2")
            a_type = aspect_data.get("aspect_type")
            if b1 and b2 and a_type:
                interp_aspect = self.get_aspect_interpretation(b1, b2, a_type)
                interpretations["aspects"].append(f"{b1} {a_type} {b2}: {interp_aspect}")

        # House Cusps
        for house_data in chart_data.get("houses", []):
            h_num = house_data.get("house_number")
            h_sign = house_data.get("sign")
            if h_num is not None and h_sign:
                interp_cusp = self.get_house_cusp_interpretation(h_num, h_sign)
                interpretations["house_cusps"].append(f"House {h_num} cusp in {h_sign}: {interp_cusp}")
        
        # Ascendant and Midheaven specific interpretations (can be treated as house cusps or special points)
        asc_data = chart_data.get("ascendant")
        if asc_data and asc_data.get("sign"):
            asc_interp = self.get_house_cusp_interpretation(1, asc_data.get("sign")) # Asc is cusp of 1st
            interpretations["house_cusps"].append(f"Ascendant in {asc_data.get('sign')}: {asc_interp}")

        mc_data = chart_data.get("midheaven")
        if mc_data and mc_data.get("sign"):
            mc_interp = self.get_house_cusp_interpretation(10, mc_data.get("sign")) # MC is cusp of 10th
            interpretations["house_cusps"].append(f"Midheaven (MC) in {mc_data.get('sign')}: {mc_interp}")

        return interpretations

# --- Example Usage (for testing) ---
if __name__ == "__main__":
    # This would typically come from chart_calculator.py
    sample_chart_data = {
        "birth_data": {
            "date": "1879-03-14", "time": "11:30", "city_country": "Ulm, Germany",
            "latitude": 48.3994, "longitude": 9.9916, "timezone_str": "Europe/Berlin",
            "utc_datetime": "1879-03-14T10:38:00+00:00", "julian_day_ut": 2407420.9430555554
        },
        "planets": [
            {"name": "Sun", "longitude": 353.79, "sign": "Pisces", "sign_long_deg": 23, "sign_min": 47, "sign_sec": 25, "is_retrograde": False, "speed": 0.99, "house_number": 10},
            {"name": "Moon", "longitude": 227.0, "sign": "Sagittarius", "sign_long_deg": 17, "sign_min": 0, "sign_sec": 0, "is_retrograde": False, "speed": 13.0, "house_number": 6},
            {"name": "Mars", "longitude": 298.0, "sign": "Capricorn", "sign_long_deg": 28, "sign_min": 0, "sign_sec": 0, "is_retrograde": False, "speed": 0.7, "house_number": 8}
        ],
        "houses": [
            {"house_number": 1, "longitude": 150.0, "sign": "Leo", "sign_long_deg": 0, "sign_min": 0, "sign_sec": 0},
            {"house_number": 10, "longitude": 60.0, "sign": "Gemini", "sign_long_deg": 0, "sign_min": 0, "sign_sec": 0}
        ],
        "aspects": [
            {"body1": "Sun", "body2": "Moon", "aspect_type": "Square", "orb": 1.2, "is_applying": None}
        ],
        "ascendant": {"longitude": 150.0, "sign": "Leo", "sign_long_deg": 0, "sign_min": 0, "sign_sec": 0},
        "midheaven": {"longitude": 60.0, "sign": "Gemini", "sign_long_deg": 0, "sign_min": 0, "sign_sec": 0}
    }

    generator = InterpretationGenerator()
    full_interpretations = generator.generate_full_interpretation(sample_chart_data)
    
    print("Generated Interpretations:")
    for category, interps in full_interpretations.items():
        if isinstance(interps, list):
            print(f"\n--- {category.replace('_', ' ').title()} ---")
            for interp in interps:
                print(f"- {interp}")
        elif isinstance(interps, str): # For error messages
             print(f"Error: {interps}")

