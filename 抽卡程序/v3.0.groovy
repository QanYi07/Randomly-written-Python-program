    #设计卡池
    #首先，需要设计卡池，包括卡池中包含哪些角色、武器或物品，以及每种物品的出现概率。可以创建一个数组或对象来表示卡池，例如：
let pool = [
  { name: '旅行者', type: '角色', probability: 0.2 },
  { name: '天空之翼', type: '武器', probability: 0.15 },
  { name: '岩王帝君', type: '角色', probability: 0.1 },
  { name: '幽夜净土', type: '武器', probability: 0.1 },
  { name: '蒲公英骑士', type: '角色', probability: 0.05 },
  { name: '风神之笛', type: '武器', probability: 0.05 },
  { name: '其他物品', type: '物品', probability: 0.3 }
];
    #生成随机数
    #在用户点击抽卡按钮时，需要生成一个随机数，用于判断抽取到哪个物品。可以使用 Math.random() 函数生成一个 0 到 1 之间的随机数，然后乘以总概率的和，再使用 Math.floor() 函数向下取整，得到一个随机的物品索引。例如：

let randomNum = Math.random();
let index = Math.floor(randomNum * pool.length);
    #获取物品信息
     #根据上一步得到的物品索引，可以从卡池中获取对应的物品信息。例如：

let item = pool[index];
console.log(您抽到了 ${item.name}！);
    #更新卡池
    #如果抽到了某个物品，需要将其从卡池中删除，避免重复抽取。可以使用 splice() 函数从卡池中删除对应物品，然后重新计算每个物品的出现概率。例如：

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
    #以上是一个简单的抽卡程序的实现思路和常用方法，具体实现可能会因为不同的需求和场景而有所不同。

