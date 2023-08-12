using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ProductWebApi.Models
{
    [Table("productItem", Schema = "dbo")]
    public class ProductItem
    {
               
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        [Key]
        [Column("ProductItemId")]
        public int ProductItemId { get; set; }

        //Relationship between Product and ProductId
        [Column("ProductId")]
        public int ProductId { get; set; }

        [ForeignKey("ProductId")]
        public Product Product { get; set; }
        [Column("Size")]
        public string Size { get; set; }
        [Column("Color")]
        public string Color { get; set; }
        [Column("Price")]
        public double Price { get; set; }
        [Column("CreatedDate")]
        public DateTime CreatedDate { get; set; }
        [Column("UpdatedDate")]
        public DateTime UpdatedDate { get; set; }
    }
}
