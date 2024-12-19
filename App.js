import React, { useState } from 'react';
import { View, Text, TextInput, Button, ScrollView, StyleSheet } from 'react-native';

const App = () => {
  const [chat, setChat] = useState('');
  const [response, setResponse] = useState('');

  const handleChat = async () => {
    try {
      const res = await fetch("http://localhost:8000/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: chat }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.navbar}>
        <Text style={styles.logo}>KTK Fitness</Text>
      </View>
      <ScrollView>
        <View style={styles.chatbot}>
          <Text>Health Chatbot</Text>
          <TextInput
            style={styles.input}
            placeholder="Ask me something..."
            value={chat}
            onChangeText={setChat}
          />
          <Button title="Send" onPress={handleChat} />
          <Text>Response: {response}</Text>
        </View>
        <View style={styles.tracker}>
          <Text>Health Tracker</Text>
          {/* Add tracker components */}
        </View>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f8f9fa' },
  navbar: { height: 60, backgroundColor: '#007bff', justifyContent: 'center', padding: 10 },
  logo: { color: '#fff', fontSize: 18, fontWeight: 'bold' },
  chatbot: { padding: 20 },
  tracker: { padding: 20 },
  input: { borderWidth: 1, padding: 10, marginBottom: 10, borderRadius: 5 },
});

export default App;
