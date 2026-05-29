export default function Testimonials() {
  const testimonials = [
    {
      name: "Priya Sharma",
      location: "Mumbai",
      text: "We found the perfect name for our daughter! The numerology analysis was spot-on and the spiritual meanings were beautiful.",
      rating: 5,
      image: "👩"
    },
    {
      name: "Rajesh Kumar",
      location: "Delhi",
      text: "As a software engineer, I was skeptical. But the AI-generated names were culturally authentic and the numerology made sense. Highly recommend!",
      rating: 5,
      image: "👨"
    },
    {
      name: "Anjali Patel",
      location: "Bangalore",
      text: "The PDF report is gorgeous! We shared it with our family and everyone loved the detailed analysis. Worth every rupee.",
      rating: 5,
      image: "👩"
    }
  ]

  return (
    <section className="py-20 bg-white">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-playfair font-bold text-darkBrown mb-4">
            What Parents Say
          </h2>
          <p className="text-xl text-gray-600">
            Join 1000+ happy parents who found their perfect name
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {testimonials.map((testimonial, index) => (
            <div 
              key={index}
              className="bg-cream/50 p-6 rounded-2xl"
            >
              {/* Rating */}
              <div className="flex gap-1 mb-4">
                {[...Array(testimonial.rating)].map((_, i) => (
                  <span key={i} className="text-gold text-xl">⭐</span>
                ))}
              </div>

              {/* Text */}
              <p className="text-gray-700 mb-6 italic">
                "{testimonial.text}"
              </p>

              {/* Author */}
              <div className="flex items-center gap-3">
                <div className="text-4xl">{testimonial.image}</div>
                <div>
                  <div className="font-semibold text-darkBrown">
                    {testimonial.name}
                  </div>
                  <div className="text-sm text-gray-600">
                    {testimonial.location}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
