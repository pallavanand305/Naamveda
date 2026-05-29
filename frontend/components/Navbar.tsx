'use client'

import Link from 'next/link'
import { useState } from 'react'
import { Menu, X } from 'lucide-react'

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <nav className="fixed top-0 w-full bg-white/95 backdrop-blur-sm shadow-sm z-50">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2">
            <span className="text-2xl">🕉️</span>
            <span className="text-2xl font-playfair font-bold text-saffron">
              Naamveda
            </span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-8">
            <Link href="/#how-it-works" className="text-darkBrown hover:text-saffron transition">
              How It Works
            </Link>
            <Link href="/#features" className="text-darkBrown hover:text-saffron transition">
              Features
            </Link>
            <Link href="/#pricing" className="text-darkBrown hover:text-saffron transition">
              Pricing
            </Link>
            <Link 
              href="/generate"
              className="px-6 py-2 bg-saffron text-white rounded-full hover:bg-saffron/90 transition"
            >
              Generate Names
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            className="md:hidden"
            onClick={() => setIsOpen(!isOpen)}
          >
            {isOpen ? <X /> : <Menu />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="md:hidden py-4 space-y-4">
            <Link 
              href="/#how-it-works" 
              className="block text-darkBrown hover:text-saffron transition"
              onClick={() => setIsOpen(false)}
            >
              How It Works
            </Link>
            <Link 
              href="/#features" 
              className="block text-darkBrown hover:text-saffron transition"
              onClick={() => setIsOpen(false)}
            >
              Features
            </Link>
            <Link 
              href="/#pricing" 
              className="block text-darkBrown hover:text-saffron transition"
              onClick={() => setIsOpen(false)}
            >
              Pricing
            </Link>
            <Link 
              href="/generate"
              className="block px-6 py-2 bg-saffron text-white rounded-full text-center"
              onClick={() => setIsOpen(false)}
            >
              Generate Names
            </Link>
          </div>
        )}
      </div>
    </nav>
  )
}
