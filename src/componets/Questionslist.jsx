import React, { useState } from 'react';

const QuestionsList = () => {
  const [questions, setQuestions] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleAddQuestion = () => {
    if (!inputValue.trim()) return;
    setQuestions([...questions, inputValue]);
    setInputValue('');
  };

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleAddQuestion();
    }
  };

  return (
    <div style={{ maxWidth: '800px', width: '100%', margin: '20px auto', padding: '30px', boxShadow: '0 4px 20px rgba(0,0,0,0.2)', borderRadius: '8px', backgroundColor: '#fff' }}>
      <div style={{ marginBottom: '30px' }}>
        <h2 style={{ color: '#333', textAlign: 'center', margin: '0 0 30px 0' }}>Build your report</h2>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <input
            type="text"
            value={inputValue}
            onChange={handleInputChange}
            onKeyPress={handleKeyPress}
            placeholder="Enter your question..."
            style={{ flex: 1, padding: '15px', border: '1px solid #ddd', borderRadius: '4px' }}
          />
          <button
            onClick={handleAddQuestion}
            style={{ backgroundColor: 'purple', color: 'white', padding: '15px 20px', border: 'none', cursor: 'pointer', borderRadius: '4px' }}
          >
            Add Question
          </button>
        </div>
      </div>
      <div>
        {questions.map((question, index) => (
          <div key={index} style={{ padding: '20px', borderBottom: '1px solid #ccc', marginTop: '20px', borderRadius: '4px', backgroundColor: '#FAF9F6' }}>
            <h4>{question}</h4>
          </div>
        ))}
        <button style={{ backgroundColor: 'purple', color: 'white', padding: '15px 20px', border: 'none', cursor: 'pointer', borderRadius: '4px', margin: '20px',justifyContent:'center' }}
        > Build Your Report</button>
      </div>

    </div>
  );
};

export default QuestionsList;
