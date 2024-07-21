using HtmlAgilityPack;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        try
        {
            var topSellers = await GetTopSellersFromSteam();
            if (topSellers == null || topSellers.Count == 0)
            {
                Console.WriteLine("Не удалось получить данные о лучших продажах.");
                return;
            }

            Console.WriteLine("Топ-10 лидеров продаж в Steam (РФ):");
            for (int i = 0; i < topSellers.Count; i++)
            {
                var game = topSellers[i];
                Console.WriteLine($"{i + 1}. {game.Name} - {game.Price}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Произошла ошибка: {ex.Message}");
        }
    }

    private static async Task<List<Game>> GetTopSellersFromSteam()
    {
        var url = "https://store.steampowered.com/search/?filter=topsellers&cc=ru";
        var client = new HttpClient();

        try
        {
            var response = await client.GetStringAsync(url);
            var htmlDoc = new HtmlDocument();
            htmlDoc.LoadHtml(response);

            var games = new List<Game>();

            var nodes = htmlDoc.DocumentNode.SelectNodes("//a[contains(@class, 'search_result_row')]");
            if (nodes == null) return null;

            foreach (var node in nodes.Take(10)) 
            {
                var nameNode = node.SelectSingleNode(".//span[contains(@class, 'title')]");
                var priceNode = node.SelectSingleNode(".//div[contains(@class, 'search_price')]");

                string name = nameNode?.InnerText.Trim() ?? "Неизвестно";
                string price = priceNode?.InnerText.Trim()?.Replace("&nbsp;", " ") ?? "Неизвестно";

                games.Add(new Game { Name = name, Price = price });
            }

            return games;
        }
        catch (HttpRequestException httpEx)
        {
            Console.WriteLine($"Ошибка HTTP при получении данных: {httpEx.Message}");
            return null;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при парсинге данных: {ex.Message}");
            return null;
        }
    }

    class Game
    {
        public string Name { get; set; }
        public string Price { get; set; }
    }
}
