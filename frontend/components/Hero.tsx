'use client'

import Link from 'next/link'
import { Sparkles } from 'lucide-react'

export default function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Background gradient */}
      <div className="absolute inset-0 spiritual-gradient opacity-10"></div>
      
      {/* Content */}
      <div className="relative z-10 container mx-auto px-4 py-20 text-center">
        {/* Om symbol */}
        <div className="text-6xl mb-6 om-symbol text-saffron">
          🕉️
        </div>
        
        {/* Main heading */}
        <h1 className="text-5xl md:text-7xl font-playfair font-bold text-darkBrown mb-6">
          Find the Perfect
          <span className="block text-saffron mt-2">Auspicious Name</span>
          <span className="block text-spiritual mt-2">For Your Child</span>
        </h1>
        
        {/* Subtitle */}
        <p className="text-xl md:text-2xl text-gray-700 mb-8 max-w-3xl mx-auto">
          AI-powered name generation combining <strong>Numerology</strong>, <strong>Astrology</strong>, 
          and <strong>Sanskrit wisdom</strong> to find names that resonate with your child's destiny
        </p>
        
        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
          <Link 
            href="/generate"
            className="px-8 py-4 bg-saffron text-white rounded-full text-lg font-semibold hover:bg-saffron/90 transition-all shadow-lg hover:shadow-xl flex items-center gap-2"
          >
            <Sparkles className="w-5 h-5" />
            Generate Names Now
          </Link>
          
          <Link 
            href="#how-it-works"
            className="px-8 py-4 bg-white text-darkBrown border-2 border-darkBrown rounded-full text-lg font-semibold hover:bg-gray-50 transition-all"
          >
            How It Works
          </Link>
        </div>
        
        {/* Social proof */}
        <div className="flex flex-wrap justify-center gap-8 text-sm text-gray-600">
          <div className="flex items-center gap-2">
            <span className="text-2xl">✅</span>
            <span>1000+ Happy Parents</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-2xl">⭐</span>
            <span>4.9/5 Rating</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-2xl">🔮</span>
            <span>Vedic Numerology</span>
          </div>
        </div>
      </div>
      
      {/* Decorative elements */}
      <div className="absolute top-20 left-10 text-6xl opacity-20 animate-pulse">✨</div>
      <div className="absolute bottom-20 right-10 text-6xl opacity-20 animate-pulse delay-1000">🌟</div>
    </section>
  )
}
