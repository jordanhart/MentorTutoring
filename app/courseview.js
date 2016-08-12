import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  View,
  TouchableOpacity,
} from 'react-native';
import { Header, Title, Container, Content, List, ListItem, Text } from 'native-base';


export default class MentorTutoring extends Component {
  constructor(props) {
    super(props);
    //listview getInitialState

  }

  render() {
          var items = ['Simon Mignolet','Nathaniel Clyne','Dejan Lovren','Mama Sakho','Emre Can'];
          return (
              <Container>
              <Header>
                    <Title>Tutoring List</Title>
                </Header>
                  <Content>
                      <List dataArray={items}
                          renderRow={(item) =>
                              <ListItem>
                                  <Text>{item}</Text>
                              </ListItem>
                          }>
                      </List>
                  </Content>
              </Container>
          );
      }
    }
