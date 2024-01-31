let pool = [
  { name: '旅行者', type: '角色', probability: 0.2 },
  { name: '天空之翼', type: '武器', probability: 0.15 },
  { name: '岩王帝君', type: '角色', probability: 0.1 },
  { name: '幽夜净土', type: '武器', probability: 0.1 },
  { name: '蒲公英骑士', type: '角色', probability: 0.05 },
  { name: '风神之笛', type: '武器', probability: 0.05 },
  { name: '其他物品', type: '物品', probability: 0.3 }
];

let randomNum = Math.random();
let index = Math.floor(randomNum * pool.length);

let item = pool[index];
console.log(您抽到了 ${item.name}！);

pool.splice(index, 1);
let totalProbability = 0;
for (let i = 0; i < pool.length; i++) {
  let item = pool[i];
  totalProbability += item.probability;
}
for (let i = 0; i < pool.length; i++) {
  let item = pool[i];
  item.probability /= totalProbability;
}


