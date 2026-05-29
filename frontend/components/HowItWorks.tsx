export default function HowItWorks() {
  const steps = [
    {
      number: "1",
      title: "Enter Details",
      description: "Provide baby's gender, date of birth, and your preferences",
      icon: "📝"
    },
    {
      number: "2",
      title: "AI Analysis",
      description: "Our AI analyzes numerology, astrology, and cultural significance",
      icon: "🤖"
    },
    {
      number: "3",
      title: "Get Names",
      description: "Receive personalized name suggestions with detailed meanings",
      icon: "✨"
    },
    {
      number: "4",
      title: "Download Report",
      description: "Get a beautiful PDF report with complete analysis",
      icon: "📄"
    }
  ]

  return (
    <section id="how-it-works" className="py-20 bg-cream/30">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-playfair font-bold text-darkBrown mb-4">
            How It Works
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Four simple steps to find the perfect name for your child
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {steps.map((step) => (
            <div key={step.number} className="text-center">
              {/* Icon */}
              <div className="text-6xl mb-4">{step.icon}</div>
              
              {/* Step number */}
              <div className="w-12 h-12 bg-saffron text-white rounded-full flex items-center justify-center text-xl font-bold mx-auto mb-4">
                {step.number}
              </div>
              
              {/* Title */}
              <h3 className="text-xl font-semibold text-darkBrown mb-2">
                {step.title}
              </h3>
              
              {/* Description */}
              <p className="text-gray-600">
                {step.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
