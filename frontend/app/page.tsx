import Hero from '@/components/Hero'
import HowItWorks from '@/components/HowItWorks'
import Features from '@/components/Features'
import Testimonials from '@/components/Testimonials'
import Pricing from '@/components/Pricing'
import CTA from '@/components/CTA'

export default function Home() {
  return (
    <main className="min-h-screen">
      <Hero />
      <HowItWorks />
      <Features />
      <Testimonials />
      <Pricing />
      <CTA />
    </main>
  )
}
