### DivideActivities
Este é um projeto em Go para dividir uma lista de atividades em dias de trabalho, de forma a maximizar o número de atividades realizadas em cada dia, respeitando o limite de horas de trabalho por dia.

# Instalação
Para instalar o projeto, basta clonar este repositório e instalar as dependências:

```bash
 git clone https://github.com/jose-cleiton/Nubank.git
 cd Nubank/Go
 go get
 ```

# Execução

 Para rodar o projeto, basta executar o arquivo main.go:

```bash
 go run DivideActivate.go
````

Você também pode compilar o projeto e gerar um binário para executá-lo:

```bash
 go build
 ./DivideActivities
````


## Configuração

As configurações de duração das atividades e o limite de horas de trabalho por dia podem ser alteradas no arquivo main.go. Basta alterar os valores das variáveis durations e hoursPerDay, respectivamente.

Por exemplo, para alterar as atividades para [1.5, 2.0, 2.5] e o limite de horas por dia para 4, basta alterar o código para:

```bash
durations := []float64{1.5, 2.0, 2.5}
hoursPerDay := 4.0
```