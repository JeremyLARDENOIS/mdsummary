# RUST

## Les bases de la programmations en RUST

Site du tuto : https://blog.guillaume-gomez.fr/Rust/

Rust en ligne : https://play.rust-lang.org/

### Hello world

```rust
fn main() {
    println!("Hello, world!");
}
```

Pour compiler ce fichier : `rustc votre_fichier.rs`

### Variables

Toutes les variables sont des constantes par défaut.

```rust
let i = 0;

i = 2; // Erreur !
```

Pour déclarer une variable mutable, il faut utiliser le mot-clé mut :

```
let mut i = 0;

i = 2; // Ok !
```
#### les types de variables

Par exemple, pour déclarer un entier de 32 bits, vous ferez :

```rust
let i: i32 = 0;
// ou :
let i = 0i32;
```

Sachez aussi que le compilateur de Rust utilise l'inférence de type. En gros, on n'est pas obligé de déclarer le type d'une variable, il peut généralement le déduire tout seul. Exemple :

```rust
let i = 0; // donc c'est un entier visiblement
let max = 10i32;

if i < max { // max est un i32, donc le compilateur en déduit que i en est un aussi
    println!("i est inférieur à max !");
}
```
voici une petite liste des différents types de base (aussi appelés "primitifs") disponibles :

- i8 : un entier signé de 8 bits
- i16
- i32
- i64
- i128
- u8 : un entier non-signé de 8 bits
- u16
- u32
- u64
- u128
- f32 : un nombre flottant de 32 bits
- f64 : un nombre flottant de 64 bits
- String
- slice (on va y revenir plus loin dans ce chapitre)

> isize et usize existent aussi et sont l'équivalent de intptr_t et de uintptr_t

#### Les slices

Pour faire simple, une slice représente un morceau de tableau. Pour ceux qui auraient fait du C/C++, c'est tout simplement un pointeur et une taille. Exemple :

```rust
let tab = &[0, 1, 2]; // tab est une slice contenant 0, 1 et 2

println!("{:?}", tab); // ça affichera "[0, 1, 2]"
let s = &tab[1..]; // s est maintenant une slice commençant à partir du 2e élément de tab
println!("{:?}", s); // ça affichera "[1, 2]"
```

### Les conditions et le pattern matching

#### Les if / else

Les if / else if / else fonctionnent de la même façon qu'en C/C++/Java :

```rust
let age: i32 = 17;

if age >= 18 {
    println!("majeur !");
} else {
    println!("mineur !");
}
```

Vous aurez noté que je n'ai pas mis de parenthèses (( et )) autour des conditions : elles sont superflues en Rust. Cependant, elles sont toujours nécessaires si vous faites des "sous"-conditions :

```rust
if age > 18 && (age == 20 || age == 24) {
    println!("ok");
}
```

Par contre, les accolades { et } sont obligatoires, même si le bloc de votre condition ne contient qu'une seule ligne de code !

En bref : pas de parenthèses autour de la condition mais accolades obligatoires autour du bloc de la condition.

#### Pattern matching

Définition wikipédia :

"Le filtrage par motif, en anglais pattern matching, est la vérification de la présence de constituants d'un motif par un programme informatique, ou parfois par un matériel spécialisé."

Pour dire les choses plus simplement, c'est une condition permettant de faire les choses de manière différente. Grâce à ça, on peut comparer ce que l'on appelle des expressions de manière plus intuitive. Ceux ayant déjà utilisé des langages fonctionnels ne devraient pas se sentir dépaysés. Comme un code vaut souvent mieux que de longues explications :

```rust
let my_string = "hello";

match my_string {
    "bonjour" => {
        println!("français");
    }
    "ciao" => {
        println!("italien");
    }
    "hello" => {
        println!("anglais");
    }
    "hola" => {
        println!("espagnol");
    }
    _ => {
        println!("je ne connais pas cette langue...");
    }
}
```

Ici ça affichera donc "anglais".

Comme vous vous en doutez, on peut s'en servir sur n'importe quel type de variable. Après tout, il sert à comparer des expressions, vous pouvez très bien matcher sur un i32 ou un f64 si vous en avez besoin.

Concernant le _, il s'agit d'une variable (nommée ainsi pour éviter un warning pour variable non utilisée, _a aurait eu le même résultat) qui contient "toutes les autres expressions". C'est en quelque sorte le else du pattern matching (il fonctionne de la même manière que le default d'un switch C/C++/Java). Cependant, il est obligatoire de le mettre si toutes les expressions possibles n'ont pas été testées ! Dans le cas présent, il est impossible de tester toutes les strings existantes, on met donc _ à la fin.
