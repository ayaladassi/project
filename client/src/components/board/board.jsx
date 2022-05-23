// const Wrapper = styled.div`
//     color: ${(props) => (props.darkMode ? 'white' : 'black')};
//     width: 100%;
//     height: 100vh;
//     background-color: ${(props) => (props.darkMode ? '#202225' : 'white')};
//   `;
//   const Game = styled.div`
//     width: 700px;
//     margin: 0 auto;
//   `;
//   const Dash = styled.span`
//     margin: 0 7px;
//   `;
//   const ScoreAndTimer = styled.div`
//     font-size: 1.5em;
//     margin: 10px 0;
//     display: flex;
//     flex-direction: row;
//     justify-content: space-between;
//   `;
//   const Score = styled.div``;
  
//   const Board = styled.div`
//     display: flex;
//     flex-wrap: wrap;
//     justify-content: space-between;
//     height: 500px;
//   `;
//   const SourceCode = styled.a`
//     position: absolute;
//     bottom: 10px;
//     left: 50%;
//     cursor: pointer;
//   `;
// export default function board(){

  
//    function initGame(seed, language, customwords){
//     let colors = [
//       'red',
//       'red',
//       'red',
//       'red',
//       'red',
//       'red',
//       'red',
//       'red',
//       'blue',
//       'blue',
//       'blue',
//       'blue',
//       'blue',
//       'blue',
//       'blue',
//       'blue',
//       'black',
//       'neutral',
//       'neutral',
//       'neutral',
//       'neutral',
//       'neutral',
//       'neutral',
//       'neutral',
//     ];
//     colors = [
//       ...colors,
//       shuffleSeed.shuffle(['red', 'blue'], seed).slice(0, 1)[0],
//     ];
//     colors = shuffleSeed.shuffle(colors, seed);

//     const words = customwords != null ? customwords : language === 'eng' ? wordList.english : wordList.dutch;
//     const cards = shuffleSeed
//       .shuffle(words, seed)
//       .slice(0, 25)
//       .map((word, i) => ({ word, found: false, color: colors[i], inverted: false }));
//     const state = { seed, cards, spymaster: false, inverted: false, redScore: 0, blueScore: 0, words: words};
//     const score = this.calculateScore(state);
//     state.redScore = score.redScore;
//     state.blueScore = score.blueScore;
//     state.language = language;
//     return state;
//   }

//   toggleSpymaster = () => {
//     this.setState((state) => {
//       const newState = {
//         spymaster: !state.spymaster,
//       };
//       //saveGame(newState);
//       return newState;
//     });
//   };

//   invertCards = () => {
//     this.setState((state) => {
//       var newCards = [...state.cards];
//       for (var i = 0; i < state.cards.length; i++) {
//         newCards[i].inverted = !state.inverted;
//       }
//       const newState = {
//         inverted: !state.inverted,
//         cards: newCards
//       }
//       return newState;
//     });
//   };


//   calculateScore = (state) => {
//     let redCount = 0;
//     let redFound = 0;
//     let blueCount = 0;
//     let blueFound = 0;
//     state.cards.forEach((card) => {
//       if (card.color === 'red') {
//         redCount += 1;
//         if (card.found) {
//           redFound += 1;
//         }
//       } else if (card.color === 'blue') {
//         blueCount += 1;
//         if (card.found) {
//           blueFound += 1;
//         }
//       }
//     });
//     return {
//       redScore: redCount - redFound,
//       blueScore: blueCount - blueFound,
//     };
//   };

//   onCardClick = (i) => {
//     this.setState((state) => {
//       const newState = JSON.parse(JSON.stringify(state));
//       if (state.cards[i].found) {
//         newState.cards[i].found = false;
//       } else {
//         newState.cards[i].found = true;
//       }
//       const score = this.calculateScore(newState);
//       newState.redScore = score.redScore;
//       newState.blueScore = score.blueScore;
//       saveGame(newState);

//       return newState;
//     });
//   };

//   startWithCustomWords = (words) => {
//     if (words == null) {
//       startNewGame();
//       return;
//     }
//     const newState = this.initGame(nanoid(), this.state.language, words);
//     this.setState(newState);
//     saveGame(newState);
//   }

//   changeLanguage = (language) => {
//     insertParam('language', language);
//     const newState = this.initGame(this.state.seed, language);
//     this.setState(newState);
//     saveGame(newState);
//     localStorage.setItem('language', language);
//   };

//   toggleDarkMode = () => {
//     this.setState((state) => {
//       const newMode = !state.darkMode;
//       localStorage.setItem('darkMode', newMode);
//       return { darkMode: newMode };
//     });
//   };

//     const {
//       redScore,
//       blueScore,
//       cards,
//       spymaster,
//       language,
//       darkMode,
//     } = this.state;
//     const cardComponents = cards.map((card, i) => (
//       <Card
//         spymaster={spymaster}
//         key={card.word}
//         color={card.color}
//         found={card.found}
//         inverted={card.inverted}
//         tabIndex={i}
//         onClick={() => this.onCardClick(i)}
//       >
//         {card.word}
//       </Card>
//     ));
//   return(
//     <Wrapper darkMode={darkMode}>
//     <Game>
  
//       <button
//         onClick={() => this.changeLanguage('eng')}
//         disabled={language === 'eng'}
//       >
//         ENG
//       </button>
//       <button
//         onClick={() => this.changeLanguage('nl')}
//         disabled={language === 'nl'}
//       >
//         NL
//       </button>
//       <ScoreAndTimer>
//         <Score>
//           <span style={{ color: '#4183cc' }}>{blueScore}</span>
//           <Dash>-</Dash>
//           <span style={{ color: '#d13030' }}>{redScore}</span>
//         </Score>
//         <Timer language={language} />
//       </ScoreAndTimer>

//       <Board>{cardComponents}</Board>
//       <div className='gameitem'>
//         <button onClick={this.toggleSpymaster}>
//           {spymaster
//             ? i18n[language].turn_off_spymaster
//             : i18n[language].turn_on_spymaster}
//         </button>
//           <button
//           style={{visibility: spymaster ? 'visible' : 'hidden' }}
//           onClick={this.invertCards}>{i18n[language].invert_cards}</button>
//       </div>
//       <button onClick={this.toggleDarkMode}>
//         {darkMode ? i18n[language].turn_off_dark_mode : i18n[language].turn_on_dark_mode}
//       </button>
//       <GameSetter 
//         startNewGame = {this.startWithCustomWords}
//         language={language}/>
//       <Instructions language={language} darkMode={darkMode} />
//     </Game>
//     <SourceCode
//       href="https://github.com/drskunk/codenames"
//       alt="Source code repository"
//     >
//       <SourceCodeImage
//         height="24"
//         viewBox="0 0 16 16"
//         version="1.1"
//         width="24"
//         aria-hidden="true"
//         darkMode={darkMode}
//       >
//         <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
//       </SourceCodeImage>
//     </SourceCode>
//   </Wrapper>





//   )  
// }
