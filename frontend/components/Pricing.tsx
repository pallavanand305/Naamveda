import Link from 'next/link'
import { Check } from 'lucide-react'

export default function Pricing() {
  return (
    <section id="pricing" className="py-20 bg-cream/30">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-playfair font-bold text-darkBrown mb-4">
            Simple, Transparent Pricing
          </h2>
          <p className="text-xl text-gray-600">
            Start free, upgrade when you're ready
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          {/* Free Plan */}
          <div className="bg-white p-8 rounded-2xl shadow-lg">
            <div className="text-center mb-6">
              <h3 className="text-2xl font-bold text-darkBrown mb-2">Free Preview</h3>
              <div className="text-5xl font-bold text-saffron mb-2">₹0</div>
              <p className="text-gray-600">Try before you buy</p>
            </div>

            <ul className="space-y-4 mb-8">
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 text-green-500 flex-shrink-0 mt-1" />
                <span>3 name suggestions</span>
              </li>
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 text-green-500 flex-shrink-0 mt-1" />
                <span>Basic numerology analysis</span>
              </li>
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 text-green-500 flex-shrink-0 mt-1" />
                <span>Destiny & soul numbers</span>
              </li>
              <li className="flex items-start gap-3 opacity-50">
                <span className="w-5 h-5 flex-shrink-0 mt-1">✗</span>
                <span>Full 10 name report</span>
              </li>
              <li className="flex items-start gap-3 opacity-50">
                <span className="w-5 h-5 flex-shrink-0 mt-1">✗</span>
                <span>PDF download</span>
              </li>
            </ul>

            <Link 
              href="/generate"
              className="block w-full py-3 bg-gray-200 text-darkBrown rounded-full text-center font-semibold hover:bg-gray-300 transition"
            >
              Try Free
            </Link>
          </div>

          {/* Premium Plan */}
          <div className="bg-gradient-to-br from-saffron to-spiritual p-8 rounded-2xl shadow-2xl text-white relative">
            <div className="absolute top-4 right-4 bg-gold text-darkBrown px-3 py-1 rounded-full text-sm font-semibold">
              Most Popular
            </div>

            <div className="text-center mb-6">
              <h3 className="text-2xl font-bold mb-2">Premium Report</h3>
              <div className="text-5xl font-bold mb-2">₹299</div>
              <p className="opacity-90">One-time payment</p>
            </div>

            <ul className="space-y-4 mb-8">
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 flex-shrink-0 mt-1" />
                <span><strong>10 personalized names</strong></span>
              </li>
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 flex-shrink-0 mt-1" />
                <span>Complete numerology analysis</span>
              </li>
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 flex-shrink-0 mt-1" />
                <span>Nakshatra compatibility</span>
              </li>
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 flex-shrink-0 mt-1" />
                <span>Spiritual blessings & meanings</span>
              </li>
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 flex-shrink-0 mt-1" />
                <span>Beautiful PDF report</span>
              </li>
              <li className="flex items-start gap-3">
                <Check className="w-5 h-5 flex-shrink-0 mt-1" />
                <span>Lifetime access</span>
              </li>
            </ul>

            <Link 
              href="/generate"
              className="block w-full py-3 bg-white text-saffron rounded-full text-center font-semibold hover:bg-gray-100 transition"
            >
              Get Premium Report
            </Link>
          </div>
        </div>

        {/* Money-back guarantee */}
        <div className="text-center mt-12">
          <p className="text-gray-600">
            ✅ 100% Satisfaction Guaranteed | 🔒 Secure Payment via Razorpay
          </p>
        </div>
      </div>
    </section>
  )
}
