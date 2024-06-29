import Navigation from "./Components/Navigation"
import Header from "./Components/Header"
import About from "./Components/About"
import WatchNow from "./Components/WatchNow"
import Features from "./Components/Features"
import OurTeam from "./Components/OurTeam"
import Testimonials from "./Components/Testimonials"
import FAQ from "./Components/FAQ"
import ContactUs from "./Components/ContactUs"

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

        <section className="download section-padding">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="sectioner-header text-center white">
                  <h3>Download Our App</h3>
                  <span className="line"></span>
                  <p className="white">Sed quis nisi nisi. Proin consectetur porttitor dui sit amet viverra. Fusce sit amet lorem faucibus, vestibulum ante in, pharetra ante.</p>
                </div>
              </div>
              <div className="col-md-12">
                <div className="section-content text-center">
                  <ul>
                    <li><a href="#"><img src="images/appstore.png" className="wow fadeInUp" data-wow-delay="0.4s"/></a></li>
                    <li><a href="#"><img src="images/playstore.png" className="wow fadeInUp" data-wow-delay="0.7s"/></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </section>

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
