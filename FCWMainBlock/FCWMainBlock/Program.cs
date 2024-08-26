void FillStringArray(int length, string[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"Введите {i + 1} строку массива: ");
        array[i] = Console.ReadLine();
    }
}
void ShowArray(string[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.WriteLine(array[i]);
    }
    Console.WriteLine();
}

string[] GetNewArray(string[] userArray)
{
    string[] newStringUserArray = new string[GetLength(userArray)];
    int discounter = 0;
    for (int i = 0; i < userArray.Length; i++)
    {
        if (userArray[i].Length <= 3) newStringUserArray[i - discounter] = userArray[i];
        else discounter++;
    }
    return newStringUserArray;
}
int GetLength(string[] userArray)
{
    int counter = 0;
    for (int i = 0; i < userArray.Length; i++)
    {
        if (userArray[i].Length <= 3)
            counter++;
    }
    return counter;
}


Console.Write("Введите натуральное число - длину массива: ");
int arrayLenght = Convert.ToInt32(Console.ReadLine());
string[] myArray = new string[arrayLenght];
FillStringArray(arrayLenght, myArray);
Console.WriteLine("Массив строк введенный пользователем:");
ShowArray(myArray);
string[] returnedArray = GetNewArray(myArray);
Console.WriteLine("Новый массив строк пользователя, длина которых меньше, либо равна 3:");
ShowArray(returnedArray);

