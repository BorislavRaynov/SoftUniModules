const chai = require('chai')
const chaiHtpp = require('chai-http')
const server = require('./server')
const exp = require('constants')
const chaiHttp = require('chai-http')
const expect = chai.expect

chai.use(chaiHttp)

describe('Books API', () => {
    let bookId;

    it('should POST a Book', (done) =>{
            const book = {id: "1", title: "Test Book", author: "Test Author"}
            chai.request(server)
                .post('/books')
                .send(book)
                .end((err, res) => {
                    expect(res).to.have.status(201)
                    expect(res.body).to.be.a('object')
                    expect(res.body).to.have.property('id')
                    expect(res.body).to.have.property('title')
                    expect(res.body).to.have.property('author')
                    bookId = res.body.id
                    done()
                })
    })

    it('should GET all books', (done) =>{
        chai.request(server)
            .get('/books')
            .end((err, res) => {
                expect(res).to.have.status(200)
                expect(res.body).to.be.a('array')
                done()
            })
    })

    it('should GET a single Book', (done) =>{
        const bookId = 1

        chai.request(server)
            .get(`/books/${bookId}`)
            .end((err, res) => {
                expect(res).to.have.status(200)
                expect(res.body).to.be.a('object')
                expect(res.body).to.have.property('id')
                expect(res.body).to.have.property('title')
                expect(res.body).to.have.property('author')
                done()
            })
    })

    it('should PUT an existing Book', (done) =>{
        const bookId = 1
        const updatedBook = {id: "1", title: "Updated Test Book", author: "Updated Test Author"}
        chai.request(server)
            .put(`/books/${bookId}`)
            .send(updatedBook)
            .end((err, res) => {
                if(err) {
                    return done(err)
                }
                expect(res).to.have.status(200)
                expect(res.body).to.be.a('object')
                expect(res.body.title).to.equal('Updated Test Book')
                expect(res.body.author).to.equal('Updated Test Author')
                done()
            })
    })

    it('should DELETE an existing Book', (done) =>{
        const deletedbookId = 1
        chai.request(server)
            .delete(`/books/${deletedbookId}`)
            .end((err, res) => {
                if(err) {
                    return done(err)
                }
                expect(res).to.have.status(204)
                done()
            })
    })

    it('should return 404 when trying GET, PUT or DELETE non-existing book', (done) =>{
        chai.request(server)
            .get('/books/9999')
            .end((err, res) => {
                if(err) {
                    return done(err)
                }
                expect(res).to.have.status(404)
            })

        chai.request(server)
        .put('/books/9999')
        .send({id: "9999", title: "None Book", author: "None Author"})
        .end((err, res) => {
            if(err) {
                return done(err)
            }
            expect(res).to.have.status(404)
        })

        chai.request(server)
        .delete('/books/9999')
        .end((err, res) => {
            if(err) {
                return done(err)
            }
            expect(res).to.have.status(404)
            done()
        })
    })
})