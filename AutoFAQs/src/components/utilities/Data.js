// const data = {
//   FITB: [
//     {
//       answer: "college",
//       id: 0,
//       question:
//         "Today the  _________ , housed in the Fitzpatrick, Cushing, and Stinson-Remick Halls of Engineering, includes five departments of study – aerospace and mechanical engineering, chemical and biomolecular engineering, civil engineering and geological sciences, computer science and engineering, and electrical engineering – with eight B.S.",
//     },
//     {
//       answer: "science",
//       id: 1,
//       question:
//         "The College of Engineering was established in 1920, however, early courses in civil and mechanical engineering were a part of the College of  _________  since the 1870s.",
//     },
//     {
//       answer: "business",
//       id: 2,
//       question:
//         "Additionally, the college offers five-year dual degree programs with the Colleges of Arts and Letters and of  _________  awarding additional B.A.",
//     },
//     {
//       answer: "master",
//       id: 3,
//       question:
//         "and  _________  of Business Administration (MBA) degrees, respectively.",
//     },
//   ],
//   MCQ: [
//     {
//       answer: "engineering",
//       distractors: [
//         "Computer Science",
//         "Aerospace",
//         "Mechatronics",
//         "Materials Science",
//       ],
//       id: 0,
//       question: "What college was established in 1920?",
//     },
//     {
//       answer: "college",
//       distractors: [
//         "High School",
//         "Senior Year",
//         "Sophomore Year",
//         "Freshman Year",
//       ],
//       id: 1,
//       question:
//         "What is the Fitzpatrick, Cushing, and Stinson-Remick Halls of Engineering?",
//     },
//     {
//       answer: "science",
//       distractors: [
//         "Scientific Method",
//         "Astrology",
//         "Evolutionary Biology",
//         "Scientific Principles",
//       ],
//       id: 2,
//       question:
//         "Civil and mechanical engineering were a part of the College of what since the 1870s?",
//     },
//     {
//       answer: "civil",
//       distractors: ["Social", "Political", "Medical", "Environmental"],
//       id: 3,
//       question:
//         "Along with mechanical engineering, what type of engineering was a part of the College of Science in the 1870s?",
//     },
//     {
//       answer: "mechanical engineering",
//       distractors: [
//         "Engineering",
//         "Computer Engineering",
//         "Computer Science",
//         "Comp Sci",
//       ],
//       id: 4,
//       question:
//         "Along with civil engineering, what engineering discipline was a part of the College of Science in the 1870s?",
//     },
//     {
//       answer: "business",
//       distractors: [
//         "Company",
//         "Large Corporation",
//         "Industry",
//         "Large Company",
//       ],
//       id: 5,
//       question:
//         "Along with the Colleges of Arts and Letters, what other degree program is offered at Notre Dame?",
//     },
//     {
//       answer: "1870s",
//       distractors: ["Late 19Th Century", "Mid-1800S"],
//       id: 8,
//       question:
//         "Since when have courses in civil and mechanical engineering been part of the College of Science?",
//     },
//     {
//       answer: "today",
//       distractors: [
//         "Yesterday",
//         "Tomorrow",
//         "Last Week",
//         "Last Night",
//         "Other Day",
//       ],
//       id: 9,
//       question: "How old is the College of Engineering?",
//     },
//   ],
//   MTF: {
//     defs: [
//       "the practical application of science to commerce or industry",
//       "the body of faculty and students of a college",
//       "a particular branch of scientific knowledge",
//     ],
//     keys: ["engineering", "college", "science"],
//   },
//   TF: [
//     {
//       answer: false,
//       id: 0,
//       sentence:
//         "The College of Engineering never was established in 1920, however, early courses in civil and mechanical engineering were a part of the College of Science since the 1870s.",
//     },
//     {
//       answer: false,
//       id: 1,
//       sentence:
//         "Additionally, the college offers five-year dual degree programs with the Colleges of Arts and Letters and of Business not awarding additional B.A.",
//     },
//     {
//       answer: true,
//       id: 2,
//       sentence:
//         "The College of Engineering was established in 1920, however, early courses in civil and mechanical engineering were a part of the College of Science since the 1870s.",
//     },
//     {
//       answer: true,
//       id: 3,
//       sentence:
//         "Today the college, housed in the Fitzpatrick, Cushing, and Stinson-Remick Halls of Engineering, includes five departments of study – aerospace and mechanical engineering, chemical and biomolecular engineering, civil engineering and geological sciences, computer science and engineering, and electrical engineering – with eight B.S.",
//     },
//     {
//       answer: true,
//       id: 4,
//       sentence:
//         "and Master of Business Administration (MBA) degrees, respectively.",
//     },
//   ],
// };

async function fetchDataAPI(
  context,
  limit,
  setError,
  setFetchedContent,
  setIsLoading
) {
  try {
    // let input = {
    //   context: context,
    //   limit: 50,
    // };
    // const api = "https://faq-generator.loca.lt/api";
    // const response = await fetch(api, {
    //   method: "POST",
    //   mode: "no-cors",
    //   credentials: "include",
    //   body: {
    //     // context: _context;
    //     context: "Delhi is the capital of India.",
    //     limit: 5,
    //   },
    // });
    let url = new URL("https://faq-generator-1.loca.lt/api");
    let params = { context: context, limit: limit };
    url.search = new URLSearchParams(params).toString();
    let response = await fetch(url);
    console.log(response);
    const cxt = await response.json();
    console.log(cxt);

    url = new URL("https://faq-generator-1.loca.lt/extra");
    params = { context: context };
    url.search = new URLSearchParams(params).toString();
    response = await fetch(url);
    console.log(response);
    const domain = await response.json();
    console.log(domain);

    const data = { context: cxt, domain: domain };
    console.log(data);
    setFetchedContent(data);
  } catch {
    setError(true);
  }
  setIsLoading(false);
}
export default fetchDataAPI;
