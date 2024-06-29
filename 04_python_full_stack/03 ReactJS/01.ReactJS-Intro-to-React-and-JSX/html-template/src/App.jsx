import Navigation from "./Components/Navigation"
import Header from "./Components/Header"
import About from "./Components/About"
import WatchNow from "./Components/WatchNow"
import Features from "./Components/Features"
import OurTeam from "./Components/OurTeam"
import Testimonials from "./Components/Testimonials"
import FAQ from "./Components/FAQ"
import ContactUs from "./Components/ContactUs"
import DownloadApp from "./Components/DownloadApp"

function App() {
  return (
    <>
        <Navigation />

        <Header />

        <About />

        <WatchNow />

        <Features />

        <OurTeam />

        <Testimonials />       

        <FAQ />

        <ContactUs />

        <DownloadApp />

        <footer className="footer-copy">
          <div className="container-fluid">
            <div className="row">
              <div className="col-md-12">
                <p>2018 &copy; Applight. Website Designed by <a href="http://w3Template.com" target="_blank" rel="dofollow">W3 Template</a></p>
              </div>
            </div>
          </div>
        </footer>
    </>
  )
}

export default App
