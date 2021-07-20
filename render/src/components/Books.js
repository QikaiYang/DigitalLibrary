//Most of the code comes from this link:
//https://www.youtube.com/watch?v=06pWsB_hoD4
import React from "react";
import { List, Header, Rating, Label } from "semantic-ui-react";

export const Books = ({books}) => {
    return(
        <List>
            {books.map(book => {
                return(
                    <List.Item key={book.title}>
                        <Header>{book.title}</Header>
                        <Rating rating={book.rating} maxRating={5}/>
                    </List.Item>
                )
            })}
        </List>
    )
}