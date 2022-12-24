const horasPorDia = 3;
const duracoes = [1.90, 1.25, 2.5, 1.75, 1.04];
let somaTempo = 0;
let diaAtual = 0;

const acharMelhorOpcao = (somaTempo, duracoesRestantes) =>
  duracoesRestantes.map(item => horasPorDia - (somaTempo + item)).filter(item => item >= 0);

const acharMinimoDeDias = duracoes => {
  const dias = [[duracoes[0]]];
  somaTempo = dias[0].reduce((soma, item) => soma + item);
  let duracoesRestantes = duracoes.slice(1);

  while (duracoesRestantes.length > 0) {
    const melhoresOpcoes = acharMelhorOpcao(somaTempo, duracoesRestantes);

    if (melhoresOpcoes.length > 0) {
      const indice = duracoesRestantes.indexOf(melhoresOpcoes[0]);
      dias[diaAtual].push(duracoesRestantes[indice]);
      somaTempo += duracoesRestantes[indice];
      duracoesRestantes = duracoesRestantes.slice(0, indice).concat(duracoesRestantes.slice(indice + 1));
    } else {
      diaAtual++;
      dias.push([]);
      somaTempo = 0;
    }
  }
  return dias.length, dias;
};

const resultado = acharMinimoDeDias(duracoes);
resultado[1].forEach((item, i) => console.log(`${i + 1} Dia `, item));
console.log('Total de dias:', resultado[0]);
