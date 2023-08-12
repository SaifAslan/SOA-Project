using Microsoft.EntityFrameworkCore;
using ProductWebApi;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
//Database Context Dependency Injection
var dbHost = Environment.GetEnvironmentVariable("DB_HOST");
var dbName = Environment.GetEnvironmentVariable("DB_NAME");
var dbPassword = Environment.GetEnvironmentVariable("DB_SA_PASSWORD");
//var dbHost = "localhost";
//var dbName = "ProductDB98";
//var dbPassword = "buket1234*";
//var connectionString = $"Data Source={dbHost};Initial Catalog={dbName};TrustServerCertificate=true;Integrated Security=True";
//var connectionString = $"Data Source={dbHost};Initial Catalog={dbName};Password={dbPassword};TrustServerCertificate=true";

var connectionString = $"Data Source={dbHost};Initial Catalog={dbName};User ID=sa; Password={dbPassword};TrustServerCertificate = true" ;


builder.Services.AddDbContext<ProductDbContext>(opt => opt.UseSqlServer(connectionString));
    
//Database Context Dependency Injection
var app = builder.Build();

// Configure the HTTP request pipeline.

app.UseAuthorization();

app.MapControllers();

app.Run();
