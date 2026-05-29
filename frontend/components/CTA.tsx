import Link from 'next/link'
import { Sparkles } from 'lucide-react'

export default function CTA() {
  return (
    <section className="py-20 spiritual-gradient">
      <div className="container mx-auto px-4 text-center">
        <div className="max-w-3xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-playfair font-bold text-white mb-6">
            Ready to Find Your Child's Perfect Name?
          </h2>
          
          <p className="text-xl text-white/90 mb-8">
            Join 1000+ parents who discovered meaningful, auspicious names with Naamveda
          </p>

          <Link 
            href="/generate"
            className="inline-flex items-center gap-2 px-8 py-4 bg-white text-saffron rounded-full text-lg font-semibold hover:bg-gray-100 transition-all shadow-lg hover:shadow-xl"
          >
            <Sparkles className="w-5 h-5" />
            Start Free Now
          </Link>

          <p className="mt-6 text-white/80 text-sm">
            No credit card required • Get 3 names free
          </p>
        </div>
      </div>
    </section>
  )
}
