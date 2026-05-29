'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { ArrowLeft, Sparkles, Loader2 } from 'lucide-react'

export default function GeneratePage() {
  const router = useRouter()
  const [loading, setLoading] = useState(false)
  const [results, setResults] = useState<any>(null)
  const [error, setError] = useState('')

  const [formData, setFormData] = useState({
    gender: 'Male',
    date_of_birth: '',
    time_of_birth: '',
    nakshatra: '',
    starting_letter: '',
    religion: 'Hindu',
    style_preference: 'Modern',
    emotional_intention: 'Success'
  })

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    setResults(null)

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/names/generate-preview`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      })

      if (!response.ok) {
        throw new Error('Failed to generate names')
      }

      const data = await response.json()
      setResults(data)
    } catch (err: any) {
      setError(err.message || 'Something went wrong. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-cream via-white to-cream/50 pt-20 pb-12">
      <div className="container mx-auto px-4">
        {/* Back Button */}
        <Link 
          href="/"
          className="inline-flex items-center gap-2 text-darkBrown hover:text-saffron transition mb-8"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to Home
        </Link>

        {/* Header */}
        <div className="text-center mb-12">
          <div className="text-5xl mb-4">🕉️</div>
          <h1 className="text-4xl md:text-5xl font-playfair font-bold text-darkBrown mb-4">
            Generate Baby Names
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Get AI-powered name suggestions based on numerology, astrology, and your preferences
          </p>
        </div>

        <div className="max-w-4xl mx-auto">
          {!results ? (
            /* Form Section */
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <form onSubmit={handleSubmit} className="space-y-6">
                {/* Gender */}
                <div>
                  <label className="block text-sm font-semibold text-darkBrown mb-2">
                    Baby Gender *
                  </label>
                  <select
                    name="gender"
                    value={formData.gender}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-saffron focus:outline-none"
                  >
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Unisex">Unisex</option>
                  </select>
                </div>

                {/* Date of Birth */}
                <div>
                  <label className="block text-sm font-semibold text-darkBrown mb-2">
                    Date of Birth *
                  </label>
                  <input
                    type="date"
                    name="date_of_birth"
                    value={formData.date_of_birth}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-saffron focus:outline-none"
                  />
                </div>

                {/* Time of Birth */}
                <div>
                  <label className="block text-sm font-semibold text-darkBrown mb-2">
                    Time of Birth (Optional)
                  </label>
                  <input
                    type="time"
                    name="time_of_birth"
                    value={formData.time_of_birth}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-saffron focus:outline-none"
                  />
                </div>

                {/* Nakshatra */}
                <div>
                  <label className="block text-sm font-semibold text-darkBrown mb-2">
                    Nakshatra (Optional)
                  </label>
                  <input
                    type="text"
                    name="nakshatra"
                    value={formData.nakshatra}
                    onChange={handleChange}
                    placeholder="e.g., Ashwini, Bharani, Rohini"
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-saffron focus:outline-none"
                  />
                </div>

                {/* Starting Letter */}
                <div>
                  <label className="block text-sm font-semibold text-darkBrown mb-2">
                    Preferred Starting Letter (Optional)
                  </label>
                  <input
                    type="text"
                    name="starting_letter"
                    value={formData.starting_letter}
                    onChange={handleChange}
                    maxLength={1}
                    placeholder="e.g., A, R, S"
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-saffron focus:outline-none uppercase"
                  />
                </div>

                {/* Religion */}
                <div>
                  <label className="block text-sm font-semibold text-darkBrown mb-2">
                    Religion/Culture *
                  </label>
                  <select
                    name="religion"
                    value={formData.religion}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-saffron focus:outline-none"
                  >
                    <option value="Hindu">Hindu</option>
                    <option value="Sikh">Sikh</option>
                    <option value="Jain">Jain</option>
                    <option value="Buddhist">Buddhist</option>
                  </select>
                </div>

                {/* Style Preference */}
                <div>
                  <label className="block text-sm font-semibold text-darkBrown mb-2">
                    Name Style *
                  </label>
                  <select
                    name="style_preference"
                    value={formData.style_preference}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-saffron focus:outline-none"
                  >
                    <option value="Modern">Modern</option>
                    <option value="Traditional">Traditional</option>
                    <option value="Unique">Unique</option>
                  </select>
                </div>

                {/* Emotional Intention */}
                <div>
                  <label className="block text-sm font-semibold text-darkBrown mb-2">
                    What do you wish for your child? *
                  </label>
                  <select
                    name="emotional_intention"
                    value={formData.emotional_intention}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-saffron focus:outline-none"
                  >
                    <option value="Success">Success & Achievement</option>
                    <option value="Peace">Peace & Tranquility</option>
                    <option value="Devotion">Devotion & Spirituality</option>
                    <option value="Prosperity">Prosperity & Wealth</option>
                    <option value="Wisdom">Wisdom & Knowledge</option>
                    <option value="Strength">Strength & Courage</option>
                  </select>
                </div>

                {/* Error Message */}
                {error && (
                  <div className="bg-red-50 border-2 border-red-200 rounded-lg p-4 text-red-700">
                    {error}
                  </div>
                )}

                {/* Submit Button */}
                <button
                  type="submit"
                  disabled={loading}
                  className="w-full py-4 bg-gradient-to-r from-saffron to-spiritual text-white rounded-lg font-semibold text-lg hover:shadow-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                >
                  {loading ? (
                    <>
                      <Loader2 className="w-5 h-5 animate-spin" />
                      Generating Names...
                    </>
                  ) : (
                    <>
                      <Sparkles className="w-5 h-5" />
                      Generate Names (Free)
                    </>
                  )}
                </button>

                <p className="text-center text-sm text-gray-500">
                  Get 3 names free • No credit card required
                </p>
              </form>
            </div>
          ) : (
            /* Results Section */
            <div className="space-y-6">
              {/* Success Message */}
              <div className="bg-green-50 border-2 border-green-200 rounded-lg p-6 text-center">
                <div className="text-4xl mb-2">✨</div>
                <h2 className="text-2xl font-bold text-green-800 mb-2">
                  Names Generated Successfully!
                </h2>
                <p className="text-green-700">
                  Here are your personalized name suggestions
                </p>
              </div>

              {/* Names */}
              {results.map((name: any, index: number) => (
                <div 
                  key={index}
                  className="bg-white rounded-2xl shadow-lg p-6 border-2 border-gold/30"
                >
                  <div className="flex items-start justify-between mb-4">
                    <div>
                      <h3 className="text-3xl font-playfair font-bold text-spiritual mb-2">
                        {index + 1}. {name.name}
                      </h3>
                      <p className="text-gray-600 italic">{name.meaning}</p>
                    </div>
                    <div className="text-right">
                      <div className="text-3xl font-bold text-saffron">
                        {name.compatibility_score}
                      </div>
                      <div className="text-sm text-gray-500">Score</div>
                    </div>
                  </div>

                  <div className="grid md:grid-cols-2 gap-4 mb-4">
                    <div className="bg-cream/50 p-4 rounded-lg">
                      <div className="text-sm font-semibold text-darkBrown mb-1">
                        Destiny Number
                      </div>
                      <div className="text-2xl font-bold text-spiritual">
                        {name.destiny_number}
                      </div>
                      <div className="text-sm text-gray-600 mt-1">
                        {name.lucky_traits?.trait}
                      </div>
                    </div>

                    <div className="bg-cream/50 p-4 rounded-lg">
                      <div className="text-sm font-semibold text-darkBrown mb-1">
                        Lucky Colors
                      </div>
                      <div className="text-lg font-semibold text-spiritual">
                        {name.lucky_traits?.lucky_color}
                      </div>
                    </div>
                  </div>

                  <div className="bg-spiritual/10 p-4 rounded-lg mb-4">
                    <div className="text-sm font-semibold text-darkBrown mb-2">
                      🕉️ Spiritual Blessing
                    </div>
                    <p className="text-gray-700 italic">
                      {name.spiritual_blessing}
                    </p>
                  </div>

                  <div className="border-t pt-4">
                    <div className="text-sm font-semibold text-darkBrown mb-2">
                      Why This Name?
                    </div>
                    <p className="text-gray-600">
                      {name.why_this_name}
                    </p>
                  </div>
                </div>
              ))}

              {/* Upgrade CTA */}
              <div className="bg-gradient-to-br from-saffron to-spiritual text-white rounded-2xl p-8 text-center">
                <div className="text-5xl mb-4">🎁</div>
                <h3 className="text-3xl font-bold mb-4">
                  Want 7 More Names?
                </h3>
                <p className="text-xl mb-6 opacity-90">
                  Get the complete premium report with 10 names, detailed analysis, and downloadable PDF
                </p>
                <div className="text-4xl font-bold mb-6">
                  ₹299 Only
                </div>
                <button
                  onClick={() => alert('Payment integration coming soon!')}
                  className="px-8 py-4 bg-white text-saffron rounded-full font-bold text-lg hover:bg-gray-100 transition-all shadow-lg"
                >
                  Unlock Premium Report
                </button>
                <p className="mt-4 text-sm opacity-75">
                  ✓ 10 Names ✓ PDF Report ✓ Lifetime Access
                </p>
              </div>

              {/* Generate Again */}
              <div className="text-center">
                <button
                  onClick={() => {
                    setResults(null)
                    setFormData({
                      gender: 'Male',
                      date_of_birth: '',
                      time_of_birth: '',
                      nakshatra: '',
                      starting_letter: '',
                      religion: 'Hindu',
                      style_preference: 'Modern',
                      emotional_intention: 'Success'
                    })
                  }}
                  className="text-saffron hover:text-spiritual font-semibold"
                >
                  ← Generate Different Names
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
