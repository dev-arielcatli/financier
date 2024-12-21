export type Expense = Readonly<{
  id: string;
  name: string;
  description: string;
  quantity: number;
  amount: number;
  date: Date | string;
  createdAt: Date | string;
  updatedAt: Date | string;
  address: string;
  tags: string[];
}>;
