def get_star_step_unlocks(mercury, saturn, north_node):
    unlocked = []

    # 🌱 Root – Security
    if mercury in ["Capricorn", "Taurus", "Virgo"]:
        unlocked.append(
            "Root – Security: You are here to create structure, stability, and grounded wisdom through your voice and mind."
        )

    # 🧡 Sacral – Expression
    if mercury in ["Aries", "Leo", "Sagittarius"]:
        unlocked.append(
            "Sacral – Expression: You are a creative force, here to express passion, emotion, and divine spark through communication."
        )

    # 💚 Heart – Connection
    if north_node in ["Cancer", "Pisces", "Scorpio"] or saturn in ["Cancer", "Pisces", "Scorpio"]:
        unlocked.append(
            "Heart – Connection: Your path is rooted in love, empathy, and nurturing meaningful emotional and energetic bonds."
        )

    # 👑 Crown – Mental Mastery
    if saturn in ["Gemini", "Libra", "Aquarius"]:
        unlocked.append(
            "Crown – Mental Mastery: You are here to master thought, logic, and the higher mind — turning ideas into impactful wisdom."
        )

    # ✨ Soul Star – Self-Awakening
    if north_node in ["Leo", "Aquarius"]:
        unlocked.append(
            "Soul Star – Self-Awakening: You carry the blueprint of divine individuality — awakening your soul gifts to uplift the collective."
        )

    return unlocked
