import './App.css';
import React, {useEffect, useState} from 'react';
import { Books } from "./components/Books"

function App() {
  const [books, setBooks] = useState([])

  useEffect(()=> {
    fetch('/books/all').then(response =>
      response.json().then(data => {
        setBooks(data);
      })
    );
  }, [])

  console.log(books)

  return (<div className="App">
    <Books books= {books}/>
  </div>);
}

export default App;
