export default function Features() {
  const features = [
    {
      icon: "🔢",
      title: "Vedic Numerology",
      description: "Calculate destiny, soul, and personality numbers using ancient Chaldean system"
    },
    {
      icon: "⭐",
      title: "Nakshatra Alignment",
      description: "Names aligned with your child's birth star for maximum auspiciousness"
    },
    {
      icon: "🕉️",
      title: "Sanskrit Meanings",
      description: "Deep, authentic meanings rooted in Sanskrit and Vedic wisdom"
    },
    {
      icon: "🎯",
      title: "Personalized AI",
      description: "GPT-4 powered suggestions tailored to your preferences and values"
    },
    {
      icon: "❤️",
      title: "Emotional Intent",
      description: "Names that embody your wishes: success, peace, wisdom, or strength"
    },
    {
      icon: "📊",
      title: "Compatibility Score",
      description: "See how well each name aligns with your child's life path"
    }
  ]

  return (
    <section id="features" className="py-20 bg-white">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-playfair font-bold text-darkBrown mb-4">
            Why Choose Naamveda?
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Combining ancient wisdom with modern AI technology
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div 
              key={index}
              className="premium-card p-6 rounded-2xl hover:shadow-xl transition-all"
            >
              <div className="text-5xl mb-4">{feature.icon}</div>
              <h3 className="text-xl font-semibold text-darkBrown mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
