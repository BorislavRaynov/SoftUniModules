const rootHtmlElement = document.getElementById('root');
const rootReactElement = ReactDOM.createRoot(rootHtmlElement);

const headingReactSectionElement = (
    <header id="site header" className='navigation'>
        <h1>Hello JSX from React</h1>
        <h2>JSX is awesome</h2>
        <p>lorem 10</p>
    </header>
);

rootReactElement.render(headingReactSectionElement);
