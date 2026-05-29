import type { Metadata } from "next"
import { Inter, Playfair_Display } from "next/font/google"
import "./globals.css"
import Navbar from "@/components/Navbar"
import Footer from "@/components/Footer"

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" })
const playfair = Playfair_Display({ 
  subsets: ["latin"], 
  variable: "--font-playfair" 
})

export const metadata: Metadata = {
  title: "Naamveda - AI-Powered Indian Baby Names",
  description: "Find the perfect auspicious name for your child with AI-powered numerology and spiritual guidance",
  keywords: "baby names, Indian names, numerology, astrology, Hindu names, Sanskrit names",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${playfair.variable} font-sans`}>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  )
}
