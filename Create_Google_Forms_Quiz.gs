// Default entry point for Google Apps Script
function myFunction() {
  createGoogleFormQuiz();
}

function createGoogleFormQuiz() {
  // 1. Create the new Google Form
  var form = FormApp.create('Diagnostic Grammar Assessment (B1–B2) | International Sales');
  form.setDescription('PRIMA LINGUA Corporate Language Training\nStudent Diagnostic Evaluation: Commercial English, Logistics & Negotiation\nTarget Benchmark: CEFR B1 / B2 Level');
  form.setIsQuiz(true);
  form.setCollectEmail(true);
  form.setAllowResponseEdits(false);
  form.setLimitOneResponsePerUser(false);
  form.setShowLinkToRespondAgain(true);

  // Section 0: Student Information
  var nameItem = form.addTextItem().setTitle('Student Full Name').setRequired(true);
  var deptItem = form.addTextItem().setTitle('Company & Department').setRequired(true);

  // Section 1: Multiple Choice
  var section1 = form.addPageBreakItem().setTitle('Part 1: Multiple Choice (15 Questions)').setHelpText('Choose the most appropriate option to complete each commercial sentence.');

  // Questions Data
  var questions = [
    {
      q: "1. Right now our sales department _______ a key contract with an overseas distributor, but normally we _______ regional retail accounts.",
      options: ["negotiates / are handling", "is negotiating / handle", "negotiates / handle", "is negotiating / are handling"],
      correct: "is negotiating / handle",
      feedback: "Temporary action happening 'right now' requires Present Continuous; regular routine ('normally') requires Present Simple."
    },
    {
      q: "2. While the export team _______ the logistics documents, the foreign buyer suddenly _______ to amend the payment terms.",
      options: ["prepared / asked", "were preparing / was asking", "were preparing / asked", "have prepared / asked"],
      correct: "were preparing / asked",
      feedback: "Past continuous ('were preparing') describes the ongoing background action interrupted by a completed event ('asked')."
    },
    {
      q: "3. I _______ with overseas distributors for five years now, but before joining this department I _______ domestic clients.",
      options: ["worked / have managed", "have worked / managed", "am working / managed", "have been working / have managed"],
      correct: "have worked / managed",
      feedback: "Unfinished duration connecting to now ('for five years now') takes Present Perfect; finished past era ('before joining') takes Past Simple."
    },
    {
      q: "4. '_______ to a major international trade fair in Germany or the Middle East?' — 'Yes, I _______ our company stand at an expo in Frankfurt two months ago.'",
      options: ["Have you ever been / attended", "Did you ever go / have attended", "Have you ever gone / attended", "Did you ever go / attended"],
      correct: "Have you ever been / attended",
      feedback: "Life experience uses 'Have you ever been'; specific past time ('two months ago') takes Past Simple ('attended')."
    },
    {
      q: "5. Our export manager looks exhausted because she _______ with our partners in Singapore nonstop since 6:00 AM.",
      options: ["is negotiating", "negotiates", "has been negotiating", "had negotiated"],
      correct: "has been negotiating",
      feedback: "Continuous action extending up to the present moment with visible result takes Present Perfect Continuous."
    },
    {
      q: "6. 'Our client just sent an email refusing our shipping terms.' — 'Don't worry, I _______ their representative right away to clarify the situation.'",
      options: ["will call", "am calling", "am going to call", "call"],
      correct: "will call",
      feedback: "Spontaneous decision made at the moment of speaking takes 'will'."
    },
    {
      q: "7. Under international export law, our department _______ provide an official certificate of origin before the shipment can clear customs.",
      options: ["should", "must / has to", "can", "might"],
      correct: "must / has to",
      feedback: "Strict legal obligation and international compliance requires 'must' or 'has to'."
    },
    {
      q: "8. If the overseas distributor _______ the full container load today, we _______ a 7% volume discount.",
      options: ["will order / provide", "orders / will provide", "orders / provide", "will order / will provide"],
      correct: "orders / will provide",
      feedback: "First conditional: If + Present Simple ('orders'), will + base verb ('will provide')."
    },
    {
      q: "9. If our company _______ more flexible credit terms to foreign buyers, we _______ much faster market share abroad.",
      options: ["offers / will gain", "offered / would gain", "offered / will gain", "would offer / gained"],
      correct: "offered / would gain",
      feedback: "Second conditional (hypothetical commercial bargaining): If + Past Simple ('offered'), would + base verb ('would gain')."
    },
    {
      q: "10. If we _______ our sales pitch to their local business culture, we _______ the distribution tender last year.",
      options: ["adapted / wouldn't lose", "had adapted / wouldn't have lost", "would adapt / didn't lose", "had adapted / wouldn't lose"],
      correct: "had adapted / wouldn't have lost",
      feedback: "Third conditional (past missed opportunity): If + Past Perfect ('had adapted'), would have + past participle ('wouldn't have lost')."
    },
    {
      q: "11. All export shipments _______ strictly according to Incoterms before they _______ to the port of entry.",
      options: ["insure / dispatch", "are insured / are dispatched", "are insuring / are dispatched", "were insured / dispatched"],
      correct: "are insured / are dispatched",
      feedback: "Present Passive Voice ('are insured / are dispatched') for standard export procedures."
    },
    {
      q: "12. This is the foreign distributor _______ warehouse network covers the entire Latin American market.",
      options: ["who", "which", "whose", "whom"],
      correct: "whose",
      feedback: "Possessive relative pronoun ('whose warehouse network')."
    },
    {
      q: "13. The client considered _______ the contract for another two years, but they refused _______ the revised price index.",
      options: ["to renew / accepting", "renewing / to accept", "to renew / to accept", "renewing / accepting"],
      correct: "renewing / to accept",
      feedback: "'Consider' takes gerund (-ing: 'renewing'); 'refuse' takes infinitive ('to accept')."
    },
    {
      q: "14. 'Could you clarify _______?'",
      options: ["when will the overseas shipment arrive", "when the overseas shipment will arrive", "when arrives the overseas shipment", "when does the overseas shipment arrive"],
      correct: "when the overseas shipment will arrive",
      feedback: "Indirect questions follow standard affirmative word order without inversion ('when the shipment will arrive')."
    },
    {
      q: "15. Our team is responsible _______ developing overseas partnerships, and our quarterly targets depend heavily _______ market stability.",
      options: ["of / on", "for / in", "for / on", "to / at"],
      correct: "for / on",
      feedback: "Fixed dependent prepositions: 'responsible for' and 'depend on'."
    }
  ];

  for (var i = 0; i < questions.length; i++) {
    var item = form.addMultipleChoiceItem();
    item.setTitle(questions[i].q).setPoints(1).setRequired(true);
    
    var choices = [];
    for (var j = 0; j < questions[i].options.length; j++) {
      var opt = questions[i].options[j];
      var isCorrect = (opt === questions[i].correct);
      choices.push(item.createChoice(opt, isCorrect));
    }
    item.setChoices(choices);
    
    var fb = FormApp.createFeedback().setText(questions[i].feedback).build();
    item.setFeedbackForIncorrect(fb);
    item.setFeedbackForCorrect(fb);
  }

  // Section 2: Error Spotting
  var section2 = form.addPageBreakItem().setTitle('Part 2: Executive Error Spotting (5 Questions)').setHelpText('Identify and type the grammatical correction for each sentence.');

  var errQuestions = [
    { q: "16. 'I am working in the overseas division since January 2021.'", ans: "I have worked (or have been working) in the overseas division since January 2021." },
    { q: "17. 'We need to discuss about the pricing policy before the meeting with our foreign client.'", ans: "We need to discuss the pricing policy..." },
    { q: "18. 'If the distributor will sign the contract by Friday, we will dispatch the first batch.'", ans: "If the distributor signs the contract by Friday..." },
    { q: "19. 'I look forward to meet you at the international trade exhibition next month.'", ans: "I look forward to meeting you..." },
    { q: "20. 'The sales director explained me the new commission structure.'", ans: "The sales director explained to me the new commission structure." }
  ];

  for (var k = 0; k < errQuestions.length; k++) {
    var textItem = form.addTextItem();
    textItem.setTitle(errQuestions[k].q).setHelpText('Type your correction below.').setPoints(1).setRequired(true);
  }

  Logger.log('====================================');
  Logger.log('GOOGLE FORM CREATED SUCCESSFULLY!');
  Logger.log('Published URL: ' + form.getPublishedUrl());
  Logger.log('Edit URL: ' + form.getEditUrl());
  Logger.log('====================================');
}
