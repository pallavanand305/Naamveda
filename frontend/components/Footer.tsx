import Link from 'next/link'

export default function Footer() {
  return (
    <footer className="bg-darkBrown text-white py-12">
      <div className="container mx-auto px-4">
        <div className="grid md:grid-cols-4 gap-8 mb-8">
          {/* Brand */}
          <div>
            <div className="flex items-center gap-2 mb-4">
              <span className="text-2xl">🕉️</span>
              <span className="text-2xl font-playfair font-bold">Naamveda</span>
            </div>
            <p className="text-gray-400">
              AI-powered Indian baby names with spiritual wisdom
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-semibold mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li>
                <Link href="/#how-it-works" className="text-gray-400 hover:text-white transition">
                  How It Works
                </Link>
              </li>
              <li>
                <Link href="/#features" className="text-gray-400 hover:text-white transition">
                  Features
                </Link>
              </li>
              <li>
                <Link href="/#pricing" className="text-gray-400 hover:text-white transition">
                  Pricing
                </Link>
              </li>
            </ul>
          </div>

          {/* Support */}
          <div>
            <h4 className="font-semibold mb-4">Support</h4>
            <ul className="space-y-2">
              <li>
                <Link href="/faq" className="text-gray-400 hover:text-white transition">
                  FAQ
                </Link>
              </li>
              <li>
                <Link href="/contact" className="text-gray-400 hover:text-white transition">
                  Contact Us
                </Link>
              </li>
              <li>
                <Link href="/privacy" className="text-gray-400 hover:text-white transition">
                  Privacy Policy
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="font-semibold mb-4">Contact</h4>
            <ul className="space-y-2 text-gray-400">
              <li>📧 support@naamveda.com</li>
              <li>📱 +91 94312 86412</li>
              <li>📍 Noida, India</li>
            </ul>
          </div>
        </div>

        {/* Bottom */}
        <div className="border-t border-gray-700 pt-8 text-center text-gray-400">
          <p>&copy; 2026 Naamveda. Made with ❤️ in Noida, India</p>
        </div>
      </div>
    </footer>
  )
}
