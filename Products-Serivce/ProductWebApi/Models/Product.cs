using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ProductWebApi.Models
{
    [Table("product",Schema ="dbo")]
    public class Product
    {
              
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        [Key]
        [Column("ProductId")]
        public int ProductId { get; set; }
        [Column("ProductName")]
        public string ProductName { get; set; }
        [Column("ProductDescription")]
        public string ProductDescription { get; set; }

        [Column("Category")]
        public string Category { get; set;}

        [Column("Price")]
        public double Price { get; set; }
        [Column("CreatedDate")]
        public DateTime CreatedDate { get; set; }
        [Column("UpdatedDate")]
        public DateTime UpdatedDate { get;  set; }

    }
}
